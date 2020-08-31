# -*- coding: utf-8 -*-

family = input()
group = input()
category = input()

dic = {
  "vertebrado": { "ave": { "carnivoro": "aguia", "onivoro": "pomba" },
                  "mamifero": { "onivoro": "homem", "herbivoro": "vaca" }},
  "invertebrado": { "inseto": { "hematofago": "pulga", "herbivoro": "lagarta" },
                    "anelideo": { "hematofago": "sanguessuga", "onivoro": "minhoca" }}
}

animal = dic[family][group][category]

print(animal)