ALL PRIVILEGES: Como vimos antes, esto le otorgaría a un usuario de MySQL acceso completo a una base de datos designada (o si no se selecciona ninguna base de datos, acceso global a todo el sistema).
CREATE: Permite crear nuevas tablas o bases de datos.
DROP: Permite eliminar tablas o bases de datos.
DELETE: Permite eliminar filas de las tablas.
INSERT: Permite insertar filas en las tablas.
SELECT: Les permite usar el comando SELECT para leer las bases de datos.
UPDATE: Permite actualizar las filas de las tablas.
GRANT OPTION: Permite otorgar o eliminar privilegios de otros usuarios.

GRANT type_of_permission ON database_name.table_name TO 'username'@'localhost';
REVOKE type_of_permission ON database_name.table_name FROM 'username'@'localhost';

SHOW GRANTS FOR 'username'@'localhost';
DROP USER 'username'@'localhost';
