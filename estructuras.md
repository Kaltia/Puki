ensure * check
  2     -installed
  3     - absent
  4     -present * exist
  5     -latest
  6 node
  7 *file
  8 *service
  9     -running
 10 user
 11 *package
 12 content (file)
 13 include *add
 14 *class *module= agrupar la configuracion de un recurso
 15 require
 16 enable
 17 hasstatus
 18 status
 19 pattern
 20 restart
 21 source
 22 notify
 23 comment
 24 home
 25 managehome
 26 
 27 -------------------------------------------------------------------------
 28 = Declaracion de un recurso Puki
 29 
 30 <resource-name>(package|service|file|user|group|whatever resource):
 31     check:installed|absent|present|latest
 32 
 33 ------------------------------------------------------------
 34 *Declaracion de un modulo Puki
 35 
 36 module <module-name>:
 37 
 38     <resource-name>:
 39         check:
 40         comment:
 41 
 42     <resource-name>:
            check:
            comment:
-------------------------------------------------------------------
#La indentacion es muy importante!

# Declaracion de un recurso tipo file en Puki

# Recurso *File*
file <nombre-del-archivo>:
  path: '/donde/se/localiza'
  
# Declaracion de un recurso tipo *service* en Puki

service <nombre-del-servicio>:
  status:<running|stoped>

# Declaracion de un recurso tipo *package* en Puki

package <nombre-del-paquete>:
  check:<installed|absent|latest>
  
# Declaracion de un *module* en Puki

module <nombre-del-modulo>:
  package <nombre-del-paquete>:
    check:<installed|absent|latest>
  
  service <nombre-del-servicio>:
    status:<running|stoped>
    
# Declaracion de un recurso tipo *user* en Puki

user <nombre-del-usuario>:
  check:<exist|absent>
  
# Declaracion de un recurso tipo *group*

group <nombre-del-grupo>:
  check:<exist|absent>