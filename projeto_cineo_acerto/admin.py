# _*_ coding: utf8 _*_
from django.contrib import admin

from corpus.models import Especialidade
from holoteca.models  import  Dominiologia_Atribut, Tipo_Atributo, Config_Atribut_ATTR
from projeto_cineo_acerto.models import  Idioma, Variavel, Termo_ou_Fraseologismo,  Entrada#, Atrib_Termo
#, Autor ,Conteudo,
#****************

     
     
  
#**************************
#class DominioInline(admin.StackedInline):
#      model =  Dominiologia_Atribut
#     fieldsets = [
#      ('Info Data', {'fields': ['variavel.','conteudo'],
#      'classes': ['collapse']}),
#      ]   
#********************
#class Atrib_TermolInline(admin.StackedInline):
#    model = Atrib_Termo
    ##fieldsets = [
    ##('Info Data', {'fields': ['atividade','assocconscic_ec','funcao','obs','ind_pagto','valor_pago','forma_pagto',
    ##'ind_presenca','percentual_presenca'],
    ##'classes': ['collapse']}),
    ##]
class VariavelInline(admin.StackedInline):
     model =  Variavel     
     #ordering = ['prioridade','sequencia']
     list_filter = ['prioridade'] 
     #fieldsets = [
     #('Info Data', {'fields': ['termo','variavel', 'conteudo', ],#'self.variavel.atributo',
     #'classes': ['collapse']# 
     #}),
     #     ]
#*********************
class VariavelAdmin(admin.ModelAdmin):
     model =  Variavel
     ordering = ['sequencia']
     list_filter = ['prioridade'] 
     inlines = [VariavelInline]
       
#********************
class EntradaInline(admin.StackedInline):
     model =  Entrada     
     fieldsets = [
          ('Detalhe', {'fields': ['termo','variavel', 'conteudo' ],'classes': ['collapse']
     }),
     ]
     #search_fields = ['conteudo']
     #list_filter = ['atrib_termo'] 

     
#********************     
class Termo_ou_FraseologismoAdmin(admin.ModelAdmin):
     model =  Termo_ou_Fraseologismo #, Config_Atribut_ATTR]
     list_filter = ['tipo_termo','idioma_orig','status_termo', 'reported_by']#, 'especialidade_central','idioma_orig'] 
     #fieldsets = [
     #   ('Remissiva', {'fields': ['remissiologia']}),
     #] Se não informar só dá display no campo informado no fieldsets
     list_display = ('nome', 'tipo_termo','status_termo', 'especialidade_central', 'idioma_orig', 'created_at', 'reported_by')
     
     search_fields = ['nome',]
     inlines = [EntradaInline]
     extra=0
     
#*****************
#class EntradaAdmin(admin.ModelAdmin):
#     model =  Entrada     
#     fieldsets = [
#     ('Info Data', {'fields': ['termo','variavel', 'conteudo', ],#'self.variavel.atributo',
#     #'classes': ['class TermoEspecialidadeInline(admin.StackedInline):
#     model = Termo_ou_Fraseologismo  collapse']# 
#     })],
#     list_filter = ['variavel'] 
             
#*************************
class TermoEspecialidadeInline(admin.StackedInline):
       model = Termo_ou_Fraseologismo  
#************************     
     
class TermoEspecialidadeAdmin(admin.ModelAdmin):
     model =  Especialidade  #, Config_Atribut_ATTR]
     search_fields = ['nome']
     list_filter = ['ordem_logica','ind_subespec'] 
     inlines = [TermoEspecialidadeInline]
     #ordering = ['sequencia']
     #extra = 01
 #********************     

 #********************
 #class Atributo_Admin(admin.ModelAdmin):
 #   model = Termo_ou_Fraseologismo #, Config_Atribut_ATTR]
 #    inlines = [DominioInline]
 #    extra = 3
   
#******************************************
admin.site.register(Especialidade,TermoEspecialidadeAdmin)
admin.site.register(Variavel)#,  VariavelAdmin)
#admin.site.register(Atrib_Termo)
#admin.site.register(Autor)
#admin.site.register(Idioma)
admin.site.register(Termo_ou_Fraseologismo, Termo_ou_FraseologismoAdmin)



#admin.site.register(Atributo_Admin)
#admin.site.register(Entrada)#,EntradaAdmin)
#admin.site.register(Conteudo)
#********************************
