# Sistema de login

usuario_correcto = 'EliasBM2006'
contraseña_correcto = '0952750933' 

print('INICIA SESION')
usuario_ingresado = input('Ingresa usuario: ')
contraseña_ingresado = input('Ingresa contraseña: ')

if usuario_ingresado == usuario_correcto:
    if contraseña_ingresado == contraseña_correcto:
        print('Sesion iniciada exitosamente.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario incorrecto.')