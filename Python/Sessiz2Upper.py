def sessizUpper(cumle):
    sesliler = "aeıioöuüAEIİOÖUÜ"
    Liste = []
    for i in cumle:
        if i not in sesliler:
            Liste.append(i.upper())

    return "".join(Liste)

print(sessizUpper("Hakan Kabasakal"))