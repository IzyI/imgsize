<template>

    <v-content>
        <v-container fluid>

            <v-row>
                <v-col class="pt-0">
                    <v-row class="justify-start" v-if="com_all_array_files.length!==0">
                        <v-col>
                            <v-card
                                    outlined
                                    class="whi"
                            >
                                <v-card-title class="text-primary">
                                    Ваши изображения
                                </v-card-title>
                                <v-card-text>

                                    <a :href="file.path" class="text--white" v-for="(file, i) in com_all_array_files"
                                       :key="i" download>
                                        <v-chip class="ma-2" label color="success">
                                            <v-icon left>mdi-file-image</v-icon>
                                            {{file.name}} <span> </span> <span class="size_color">({{file.old_size}} Kb => {{file.new_size}} Kb)</span>
                                        </v-chip>
                                    </a>


                                </v-card-text>
                                <v-card-actions>
                                    <v-btn class="ma-2" tile color="accent" v-on:click="deleteFiles">
                                        <v-icon small>mdi-delete</v-icon>
                                        Удалить
                                    </v-btn>

                                    <v-btn class="ma-2" tile color="primary" v-on:click="exportZip">
                                        <v-icon small>mdi-arrow-down-bold-hexagon-outline</v-icon>
                                        Скачать Архивом
                                    </v-btn>

                                </v-card-actions>

                            </v-card>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col class="d-flex justify-center">
                            <v-card
                                    class="w100"
                            >
                                <v-img
                                        height="200px"
                                        width="100%"
                                        src="https://i.picsum.photos/id/381/2000/200.jpg"
                                        blu
                                >
                                    <v-card-title class="font-weight-bold"><a href="/" class="bcx">IMG-Size</a>
                                    </v-card-title>
                                    <v-card-subtitle class="pb-0"><a href="/" class="bcx">Не больше 20 изображений в
                                        день на
                                        одного
                                        юзера.</a>
                                    </v-card-subtitle>
                                </v-img>


                                <v-card-text class="text--primary">
                                    <v-row v-if="com_all_array_images.length!==0">

                                        <v-col>
                                            <v-row class="">
                                                <v-col cols="6" lg="2" md="3" sm="3" class="text-center "
                                                       v-for="(image, i) in com_all_array_images"
                                                       :key="i">
                                                    <div>
                                                        <div class="figrib pa-1">
                                                            <v-img max-height="100px" max-width="100%"
                                                                   class=" pa-1 mb-3"
                                                                   :src="image.file"/>
                                                        </div>
                                                        <div class="d-flex justify-space-around mt-1 mb-1 ">
                                                            <v-btn class="btmfdfgrerav" x-small dark color="accent"
                                                                   v-on:click="removeImage(i)">
                                                                <v-icon small>mdi-delete</v-icon>
                                                            </v-btn>
                                                            <v-btn class="btmfdfgrerav" x-small dark color="success"
                                                                   v-on:click="get_info(i)">
                                                                <v-icon small>mdi-pencil</v-icon>
                                                            </v-btn>
                                                        </div>
                                                    </div>
                                                </v-col>
                                            </v-row>
                                        </v-col>
                                    </v-row>
                                    <v-row v-else>
                                        <v-col>
                                            <div>Сервис предостовялетя возможность сжатие картинок на базе библиотеки
                                                Mozilla JPEG.
                                            </div>
                                            <div>Так же есть возможность обрезать и отмаштабировать изображение.</div>
                                            <div> С кодом можно ознакомится на: <a
                                                    href="https://github.com/IzyI/imgsize" target="_blank">https://github.com/IzyI/imgsize</a>
                                            </div>
                                        </v-col>

                                    </v-row>


                                </v-card-text>

                            </v-card>
                        </v-col>

                    </v-row>


                    <v-row>
                        <v-col class="text-center">
                            <v-btn @click.stop="loggout" tile color="warning">Выход</v-btn>
                        </v-col>
                        <v-col class="text-center">
                            <v-btn tile outlined color="accent" v-on:click="deleteImage">
                                <v-icon small>mdi-block-helper</v-icon>
                                Очистить
                            </v-btn>
                        </v-col>
                        <v-col class="text-center">
                            <v-btn tile outlined color="success" @click="$refs.inputUpload.click()">
                                <v-icon small>mdi-folder-multiple-image</v-icon>
                                Загрузить
                            </v-btn>
                            <input v-show="false" ref="inputUpload" type="file" @change="onFileChange" multiple>
                        </v-col>

                        <v-col class="text-center">
                            <v-btn tile outlined color="secondary" v-on:click="uploadHere">
                                <v-icon small>mdi-arrow-right-bold-hexagon-outline</v-icon>
                                Отправить
                            </v-btn>
                        </v-col>

                    </v-row>


                </v-col>
            </v-row>


        </v-container>
        <!-----------------------------------------------ДИАЛОГОВЫЕ-ОКНА------------------------------------------------------->
        <!---------------Информация---------------------------------->
        <v-dialog
                v-model="info"
                max-width="1000px"
                class="body-2 rd"
                light

        >
            <v-card>
                <v-card-title class="subtitle-2">
                    <v-spacer></v-spacer>
                    Информация
                    <v-spacer></v-spacer>
                </v-card-title>
                <v-card-text>
                    <v-container class="trin_vcrop">
                        <vue-cropper ref="cropper"
                                     :img="image"
                                     :output-size="option.size"
                                     :output-type="option.outputType"
                                     :info="true"
                                     :full="option.full"
                                     :can-move="option.canMove"
                                     :can-move-box="option.canMoveBox"
                                     :fixed-box="option.fixedBox"
                                     :original="option.original"
                                     :auto-crop="option.autoCrop"
                                     :center-box="option.centerBox"
                                     :high="option.high"
                                     @real-time="realTime"

                                     @img-load="imgLoad"
                        ></vue-cropper>
                    </v-container>

                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>

                    <v-btn @click="rotateLeft" class="mx-2" fab dark small color="secondary">
                        <v-icon dark>mdi-rotate-left</v-icon>
                    </v-btn>
                    <v-btn @click="rotateRight" class="mx-2" fab dark small color="secondary">
                        <v-icon dark>mdi-rotate-right</v-icon>
                    </v-btn>
                    <v-btn @click="changeScale(1)" class="mx-2" fab dark small color="secondary">
                        <v-icon dark>mdi-plus-circle-outline</v-icon>
                    </v-btn>
                    <v-btn @click="changeScale(-1)" class="mx-2" fab dark small color="secondary">
                        <v-icon dark>mdi-minus-circle-outline</v-icon>
                    </v-btn>
                    <v-btn
                            color="error"
                            @click="info = false"
                            small
                    >
                        Закрыть
                    </v-btn>
                    <v-btn
                            color="primary"
                            @click="saveImage"
                            small
                    >
                        Сохранить
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>


    </v-content>


</template>

<script>
    import myutils from "../../myutils";
    // import saveAs from "file-saver"


    export default {
        name: "ImgSize",
        props: {},
        data: () => ({
            image: "",
            info: false,
            image_id: 0,
            previews: {},
            option: {
                size: 1,
                full: false,  //  ?
                canMove: true, //  можно ли перемещать загруженное изображение
                canMoveBox: true, //  можно ли перемещать выделенное изображение
                fixedBox: false, //  ?
                original: true, //  при открытии грузится оригинал или увеличивается
                autoCrop: true, //  сразу ли включен кроп
                centerBox: true, // ограниченгго ли пое снимка загруженным изображением
                high: false
            },
        }),
        methods: {
            saveImage() {

                this.$refs.cropper.getCropData((data) => {
                    this.$store.dispatch(
                        "ac_replace_array_images",
                        {
                            file: data, id: this.image_id
                        }
                    );
                    this.info = false;
                })
            },

            rotateLeft: function () {
                this.$refs.cropper.rotateLeft()
            },
            rotateRight: function () {
                this.$refs.cropper.rotateRight()
            },
            changeScale: function (num) {
                num = num || 1;
                this.$refs.cropper.changeScale(num)
            },
            loggout: function () {
                this.$router.push({name: 'Logout'})
            },

            get_info: function (id) {
                this.image = this.$store.state.images.array_images[id].file;
                this.image_id = id;
                this.info = true;
            },
            realTime(data) {
                this.previews = data;
                // console.log(data)
            },
            imgLoad(msg) {
                console.log(msg, "imgLoad")
            },
            uploadHere() {
                var loader = this.$loading.show({});
                let v = this;
                v.$store.dispatch("ac_upload_array_images").then(function () {
                    v.$store.dispatch('ac_allFiles',).then(function () {
                    }).catch(function (err) {
                        myutils.notifError(v, err);
                    })
                }).catch(function (err) {
                    myutils.notifError(v, err);
                    v.$store.dispatch('ac_allFiles',).then(function () {
                    }).catch(function (err) {
                        myutils.notifError(v, err);
                    })
                }).finally(
                    function () {
                        loader.hide();
                    });


            },
            onFileChange(e) {
                this.createImages(e.target.files || e.dataTransfer.files)
            },
            createImages(files) {
                var loader = this.$loading.show({});
                let v = this;
                [...files].forEach(function callback(file) {
                    if (/\.(jpe?g|png|gif)$/i.test(file.name) === false) {
                        myutils.notifError(v, "Файл " + file.name + " не является изображением");
                        loader.hide()
                        return
                    }
                    const reader = new FileReader();
                    reader.onload = function (e) {
                        v.$store.dispatch("ac_add_array_images", {file: e.target.result, name: file.name});
                    };
                    reader.readAsDataURL(file);

                });
                loader.hide();
            },
            removeImage(index) {
                this.$store.dispatch("ac_del_slice_array_images", index);
            },
            deleteImage() {
                this.$store.dispatch("ac_set_array_images", []);
            },
            deleteFiles() {
                this.$store.dispatch("ac_delFiles");
            },


            exportZip() {
                var v = this;
                var loader = this.$loading.show({});
                this.$store.dispatch('ac_ExportZIP').then(function (arrData) {
                    loader.hide();

                    var fileURL = window.URL.createObjectURL(new Blob([arrData.data]));
                    var fileLink = document.createElement('a');

                    fileLink.href = fileURL;
                    fileLink.setAttribute('download', 'file.zip');
                    document.body.appendChild(fileLink);
                    fileLink.click();
                }).catch(function (err) {
                    loader.hide();
                    console.log(err)
                    myutils.notifError(v, err);

                })

            },

        },
        watch: {
            $route() {

            }
        },
        computed: {
            com_all_array_images: function () {
                return this.$store.state.images.array_images
            },
            com_all_array_files: function () {
                return this.$store.state.images.array_files
            },
        },
        created() {
            let loader = this.$loading.show({});
            let v = this;
            this.$store.dispatch('ac_allFiles',).then(function () {
            }).catch(function (err) {
                myutils.notifError(v, err);
            }).finally(
                function () {
                    loader.hide();
                });

        }
    }
</script>

<style lang="scss">

    input[type="file"] {
        display: none;
    }

    .trin_vcrop {
        min-width: 100%;
        height: 500px;

    }


    .custom-file-upload {
        border: 1px solid #ccc;
        border-radius: 3px;
        display: inline-block;
        padding: 6px 12px;
        cursor: pointer;
    }

    .btmfdfgrerav {
        min-width: 49px !important;
    }

    .by64uu {
        display: block;
        min-height: 300px;
        min-width: 100%;
    }


    .vue-cropper {
        background-repeat: repeat;
    }

    .bcx {

        color: #265463 !important;
        text-decoration: none !important;
    }

    .whi {
        border-color: rgb(19, 112, 33) !important;
    }

    .text-primary {
        color: rgb(19, 112, 33) !important;
    }

    .size_color {
        color: #0c3b80 !important;
        caret-color: #0c3b80 !important;
    }

    .figrib {
        border: 1px solid #1a2d332e;
    }


</style>