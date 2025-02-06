def calcular_recursos_brawler(nivel_actual, nivel_deseado, gadgets, star_powers, hypercharge, refuerzos=0):
    """No se tienen en cuenta refuerzos míticos o épicos.
    Función que recibe los parámetros del brawler que se desea subir de nivel y devuelve los recursos necesarios para ello.
    Args:
        nivel_actual (int): Nivel actual del brawler.
        nivel_deseado (int): Nivel al que se desea subir el brawler.
        gadgets (int): Cantidad de gadgets que se desean comprar.
        star_powers (int): Cantidad de star powers que se desean comprar.
        hypercharge (bool): Indica si se desea comprar la hipercarga.
        refuerzos (int): Cantidad de refuerzos que se desean comprar.
    Returns:
        monedas (int): Cantidad de monedas necesarias para subir de nivel el brawler.
        puntos_fuerza (int): Cantidad de puntos de fuerza necesarios para subir de nivel el brawler.
    """
    ## Comprobaciones de integridad

    assert nivel_actual >= 1 and nivel_actual <= 11
    assert nivel_deseado >= 2 and nivel_deseado <= 11
    assert nivel_actual <= nivel_deseado
    assert isinstance(gadgets, int) and gadgets >= 0 and gadgets < 3
    assert isinstance(star_powers, int) and star_powers >= 0 and star_powers <= 2
    assert isinstance(hypercharge, bool)
    assert isinstance(refuerzos, int) and refuerzos >= 0 and refuerzos < 6

    ### Recursos necesarios para subir de nivel
    level = [(20, 20), (35, 30), (75, 50), (140, 80), (290, 130), (480, 210), (800, 340), (1250, 550), (1875, 890), (2800, 1440)]
    
    monedas = 0
    puntos_fuerza = 0

    #### Cálculos nivel
    for i in range(nivel_actual, nivel_deseado):
        monedas += level[i - 1][0]
        puntos_fuerza += level[i - 1][1]
    
    #### Cálculos gadgets
    monedas += gadgets * 1000

    #### Cálculos star powers
    monedas += star_powers * 2000

    #### Cálculos hypercharge
    if hypercharge:
        monedas += 5000
    
    #### Cálculos refuerzos
    for i in range(refuerzos):
        monedas += 1000
    
    return monedas, puntos_fuerza

if __name__ == "__main__":
    print(calcular_recursos_brawler(9, 11, 0, 1, True, 0))