# src/sql/sql_queries.py

GET_STUDENT_BY_CARNET= "SELECT CARNET, NOMBRE, PROGRAMA FROM matriculas WHERE CARNET = %s"

GET_AUTH_LOGIN= """
    SELECT 
    USUARIO_ACCESO, 
    CLAVE_ACCESO
    FROM USUARIO_SISTEMA 
    WHERE USUARIO_ACCESO = %s
    AND CAST(AES_DECRYPT(CLAVE_ACCESO, SHA2('B!1w8*NAt1T^%%kvhUI*S^_', 512)) AS CHAR(30)) = %s 
"""
# GET_AUTH_LOGIN="""    
#     SELECT 
#     USUARIO_ACCESO, 
#     CLAVE_ACCESO 
#     FROM USUARIO_SISTEMA 
#     WHERE USUARIO_ACCESO = %s
# """

# Querys Cantidad de desertores de forma general
GET_CANT_DESERTORES_BY_GENERO= """
    SELECT 
    GENERO, 
    COUNT(DISTINCT NUMERO_DOCUMENTO) AS cantidad_estudiantes
    FROM matriculas
    WHERE DESERTO LIKE '%Desertor%'
    GROUP BY GENERO
"""
GET_CANTIDAD_DESERTORES_Y_PORCEN= """
    SELECT 
        COUNT(DISTINCT CARNET) AS cantidad_estudiantes,
        ROUND((COUNT(DISTINCT CARNET) * 100.0 / 
        (SELECT COUNT(DISTINCT CARNET) FROM matriculas)), 2) AS porcentaje_desercion 
    FROM matriculas 
    WHERE DESERTO LIKE '%Desertor%'
"""
GET_CANT_DESERTORES_BY_FACULTAD= """
    SELECT 
    FACULTAD, 
    COUNT(DISTINCT CARNET) AS cantidad_estudiantes_desertores
    FROM matriculas
    WHERE DESERTO LIKE '%Desertor%'
    GROUP BY FACULTAD;
"""

GET_CANT_DESERTORES_BY_SISBEN= """
    SELECT 
    SISBEN, 
    COUNT(DISTINCT NUMERO_DOCUMENTO) AS cantidad_estudiantes_desertores
    FROM matriculas
    WHERE DESERTO LIKE '%Desertor%'
    GROUP BY SISBEN
"""

GET_CANT_DESERTORES_BY_PAIS= """
    SELECT 
    PAIS, 
    COUNT(DISTINCT NUMERO_DOCUMENTO) AS cantidad_estudiantes_desertores
    FROM matriculas
    WHERE DESERTO LIKE '%Desertor%'
    GROUP BY PAIS;
"""

GET_CANT_DESERTORES_BY_ETNIA="""
    SELECT 
    GRUPO_ETNICO, 
    COUNT(DISTINCT NUMERO_DOCUMENTO) AS cantidad_estudiantes_desertores
    FROM matriculas
    WHERE DESERTO LIKE '%Desertor%'
    GROUP BY GRUPO_ETNICO
"""

GET_CANT_DESERTORES_BY_NIVEL_EDU_PADRE="""
    SELECT 
        NIVEL_EDU_PADRE,  
        COUNT(DISTINCT NUMERO_DOCUMENTO) AS cantidad_estudiantes_desertores
    FROM matriculas
    WHERE DESERTO LIKE '%Desertor%'
    GROUP BY NIVEL_EDU_PADRE;
"""

GET_CANT_DESERTORES_BY_NIVEL_EDU_MADRE="""
    SELECT 
        NIVEL_EDU_MADRE,  
        COUNT(DISTINCT NUMERO_DOCUMENTO) AS cantidad_estudiantes_desertores
    FROM matriculas
    WHERE DESERTO LIKE '%Desertor%'
    GROUP BY NIVEL_EDU_MADRE
"""

GET_PORCENTAJE_DESERTORES_BY_FACULTAD="""
    SELECT 
        FACULTAD, 
        COUNT(DISTINCT CASE WHEN DESERTO LIKE '%Desertor%' THEN NUMERO_DOCUMENTO END) AS cantidad_estudiantes_desertores,
        COUNT(DISTINCT NUMERO_DOCUMENTO) AS total_estudiantes,
        ROUND(
            (COUNT(DISTINCT CASE WHEN DESERTO LIKE '%Desertor%' THEN NUMERO_DOCUMENTO END) * 100.0 / COUNT(DISTINCT NUMERO_DOCUMENTO)),
            2
        ) AS porcentaje_desercion
    FROM matriculas
    GROUP BY FACULTAD
"""