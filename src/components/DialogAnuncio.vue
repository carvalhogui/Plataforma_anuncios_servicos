<template>
  <v-dialog :value="value" @input="$emit('input', $event)" width="1000">
    <v-card outilined>
      <v-card-title class="grey lighten-4">
        <div
          class="d-flex justify-space-between align-center"
          style="width: 100%"
        >
          <div class="d-flex align-center">
            <v-icon left color="#1c4163">mdi-plus</v-icon>
            <span>Cadastre seu anúncio!</span>
          </div>
          <v-icon @click="closeDialog()">mdi-close</v-icon>
        </div>
      </v-card-title>
      <v-card-text class="mt-4">
        <!-- ********IDENTIFICAÇÃO ********-->
        <div class="d-flex align-center">
          <v-icon>mdi-identifier</v-icon>
          <h3>Quem é você?</h3>
        </div>
        <v-divider class="mt-1 mb-4"></v-divider>
        <v-form ref="form">
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                hide-details
                outlined
                v-model="form.nome"
                label="Nome completo"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                hide-details
                outlined
                v-model="form.email"
                label="Email"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                hide-details
                outlined
                v-model="form.dataNascimento"
                label="Data de nascimento"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                hide-details
                outlined
                v-model="form.cpf"
                label="CPF"
              >
              </v-text-field>
            </v-col>
          </v-row>
          <!-- ********LOCALIZAÇÃO ********-->
          <div class="d-flex align-center mt-3">
            <v-icon left>mdi-map-marker-check-outline</v-icon>
            <h3>Onde está localizado?</h3>
          </div>
          <v-divider class="mt-1 mb-4"></v-divider>
          <v-row>
            <v-col cols="12" sm="4">
              <v-text-field
                hide-details
                outlined
                v-model="form.cep"
                label="CEP"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                hide-details
                outlined
                v-model="form.rua"
                label="Logradouro"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="2">
              <v-text-field
                hide-details
                outlined
                v-model="form.numero"
                label="Número"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="4">
              <v-text-field
                hide-details
                outlined
                v-model="form.bairro"
                label="Bairro"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="4">
              <v-text-field
                hide-details
                outlined
                v-model="form.cidade"
                label="Cidade"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="4">
              <v-text-field
                hide-details
                outlined
                v-model="form.estado"
                label="Estado"
              >
              </v-text-field>
            </v-col>
          </v-row>
          <div class="d-flex align-center mt-3">
            <v-icon left>mdi-newspaper-check</v-icon>
            <h3>O que deseja anunciar?</h3>
          </div>
          <v-divider class="mt-1 mb-4"></v-divider>
          <v-row>
            <v-col cols="12" sm="8">
              <v-text-field
                hide-details
                outlined
                v-model="form.titulo"
                label="Escolha um título para o anúncio"
              >
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="4">
              <v-autocomplete
                :items="categorias"
                hide-details
                outlined
                v-model="form.categoria"
                label="Categoria"
              >
              </v-autocomplete>
            </v-col>
            <v-col cols="12" sm="12">
              <v-textarea
                clearable
                counter="200"
                hide-details
                outlined
                v-model="form.descicaoservico"
                label="Descreva o serviço que deseja oferecer..."
              >
              </v-textarea>
            </v-col>
          </v-row>
        </v-form>
        <div class="caption mt-3">Campos com * são obrigatórios</div>
        <v-divider class="my-3" />
        <div class="d-flex justify-space-between align-center">
          <v-btn outlined color="secondary">
            <v-icon left>mdi-arrow-u-left-top</v-icon>
            <span>Voltar</span>
          </v-btn>
          <v-btn color="success" depressed>
            <v-icon left>mdi-floppy</v-icon>
            <span>Cadastrar</span>
          </v-btn>
        </div>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "DiagloAnuncio",
  props: {
    value: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
    categorias: [
      "Engenharia",
      "Jardinagem",
      "Programação",
      "Serviços domésticos",
    ],
    form: {
      nome: null,
      email: null,
      dataNascimento: null,
      cpf: null,
      cep: null,
      rua: null,
      numero: null,
      bairro: null,
      cidade: null,
      estado: null,
      titulo: null,
      categoria: null,
      descicaoservico: null,
    },
  }),
  methods: {
    closeDialog() {
      // this.$refs?.usuariosFormCriar?.resetForm();
      this.$emit("input", false);
    },
  },
});
</script>
