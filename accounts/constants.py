

class Specializare:
    MATEMATICA = 'M'
    INFORMATICA = 'I'
    MATEMATICA_INFORMATICA = 'MI'

    CHOICES = {
        (MATEMATICA, 'Matematică'),
        (INFORMATICA, 'Informatică'),
        (MATEMATICA_INFORMATICA, 'Matematică-Informatică'),
    }


class LimbaPredare:
    ROMANA = 'R'
    MAGHIARA = 'M'
    ENGLEZA = 'E'
    GERMANA = 'G'
    
    CHOICES = {
        (ROMANA, 'Română'),
        (MAGHIARA, 'Maghiară'),
        (ENGLEZA, 'Engleză'),
        (GERMANA, 'Germană'),
    }

class An:
    UNU = 1
    DOI = 2
    TREI = 3
    
    CHOICES = {
        (UNU, 'I'),
        (DOI, 'II'),
        (TREI, 'III')
    }
    
    