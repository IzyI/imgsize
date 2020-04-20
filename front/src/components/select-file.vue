<script>
export default {
  name: 'VSelectFile',
  model: {
    prop: 'value',
    event: 'change'
  },
  props: {
    label: {
      type: String,
      default: ''
    },
    value: {
      type: Array,
      default: null
    },
    accept: {
      type: String,
      default: null
    },
    disabled: {
      type: Boolean,
      default: false
    },
    rules: {
      type: Array,
      default() {
        return []
      }
    },
    fetch: {
      type: Function,
      default: null
    }
  },
  data() {
    return {
      items: this.value ? this.value.slice() : [],
      dialog: false,
      data: null,
      type: null,
      selected_: null
    }
  },
  computed: {
    selected: {
      get() {
        return this.selected_
      },
      set(value) {
        if (this.data) {
          URL.revokeObjectURL(this.data)
        }

        if (value) {
          this.data = URL.createObjectURL(value.file || value.blob)
          this.type = value.type
          this.dialog = true
        } else {
          this.dialog = false
          this.type = null
          this.data = null
        }

        this.selected_ = value
      }
    }
  },
  beforeDestroy() {
    this.selected = null
  },
  methods: {
    clicked() {
      this.$refs.input.click()
    },
    changed(files) {

      if (files.length === 0) {
        return
      }

      const types = this.accept ? this.accept.split(',') : []

      let update = false

      for (let i = 0, file, push; i < files.length; i++) {
        file = files[i]

        push = this.accept === null ? true : false

        for (let j = 0, type; j < types.length; j++) {
          type = types[j].trim()

          if (type === file.type ||
              type.endsWith('*') &&
              file.type.startsWith(type.substring(0, type.length - 1))) {

            push = true
            break
          }
        }

        for (let j = 0, item; j < this.items.length; j++) {
          item = this.items[j]

          if (item.name === file.name) {
            push = false
            break
          }
        }

        if (push) {
          this.items.push({
            name: file.name,
            type: file.type,
            size: file.size,
            file
          })
          update = true
        }
      }

      this.$refs.input.value = ''

      if (update) {
        this.update()
      }
    },
    remove(index) {
      this.items.splice(index, 1)
      this.update()
    },
    update() {
      this.$emit('change', this.items.slice())
    },
    preview(item) {
      if (item.file || item.blob) {
        this.selected = item
      } else if (this.fetch) {
        this.fetch(item).then(() => this.selected = item)
      }
    }
  }
}
</script>

<template>
  <div class="select-file">
    <input
      ref="input"
      type="file"
      multiple
      :accept="accept"
      :disabled="disabled"
      @change="changed($event.target.files)">

    <v-select
      v-model="items"
      append-icon="mdi-arrow-down-bold-hexagon-outline"
      readonly
      item-text="name"
      item-value="name"
      return-object
      multiple
      :disabled="disabled"
      :rules="rules"
      :label="label"
      :items="items"
      :append-icon-cb="clicked">
      <template
        slot="selection"
        slot-scope="props">
        <v-chip
          class="chip--select-multi"
          close
          :key="props.item.name"
          :selected="props.selected"
          @input="remove(props.index)"
          @click="preview(props.item)">{{ props.item.name }}</v-chip>
      </template>
    </v-select>

    <v-dialog
      v-model="dialog"
      transition="dialog-bottom-transition"
      fullscreen
      scrollable
      hide-overlay>
      <v-card>
        <v-toolbar
          dark
          color="primary">
          <v-btn
            icon
            dark
            @click="selected = null">
            <v-icon>md-close</v-icon>
          </v-btn>
          <v-toolbar-title>{{ label }}</v-toolbar-title>
        </v-toolbar>

        <template v-if="data !== null && type !== null">
          <embed
            v-if="type === 'application/pdf'"
            class="view-pdf"
            :type="type"
            :src="data"
            :key="data">

          <v-card-text v-else-if="type.substring(0, 6) === 'image/'"><img
            :src="data"
            :key="data">
          </v-card-text>

          <v-card-text v-else><v-alert
            type="error"
            :value="true">{{ type }} not supported.</v-alert>
          </v-card-text>
        </template>

      </v-card>
    </v-dialog>

  </div>
</template>

<style scoped>
  .view-pdf {
    width: 100%;
    height: 100%;
  }

  .select-file input[type=file] {
    position: absolute;
    filter: alpha(opacity=0);
    opacity: 0;
  }
</style>