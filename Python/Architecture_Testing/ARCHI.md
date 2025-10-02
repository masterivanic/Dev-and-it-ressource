# 💰 **Bank Account** 💰
🌐 Disponible en :  
[🇫🇷 Français](README.md) | [🇬🇧 English](README.en.md)

# Sujet

Ce kata est un challenge d'[architecture hexagonale](https://fr.wikipedia.org/wiki/Architecture_hexagonale) autour du domaine de la banque.

## ⚠️ Modalités de candidatures ⚠️

> Ce kata a deux objectifs : 
> - d'une part, permettre votre évaluation technique en tant que candidat ; 
> - d'autre part servir de base à votre montée en compétences si vous nous rejoignez :smile:.
> 
> Il a donc volontairement un scope très large.
> 
> **Dans le premier cas (processus de recrutement), nous comprenons que le temps est une ressource précieuse et limitée. 
> C'est pourquoi nous vous proposons trois niveaux d'engagement, selon le temps que vous pouvez y consacrer :**
>
> 1. vous avez peu de temps (une soirée) : Concentrez-vous uniquement sur le code métier. 
>   - Assurez-vous qu'il est testé et fonctionnel, avec des adapteurs de tests. 
>   - **Nous ne vous tiendrons pas rigueur de ne pas avoir réalisé les autres parties.** 
>   - **Nous aborderons ensemble les éléments non couverts lors de l'entretien technique**
> 2. vous avez plus de temps (plusieurs soirées) : le code métier, exposé derrière une api REST, et une persistance fonctionnelle ; le tout testé de bout en bout.
> 3. vous avez beaucoup de temps, et envie d'aller plus loin : la même chose, avec la containerisation de l'application, et une pipeline de CI/CD ;
> 
> Vous serez évalués notamment sur les points suivants :
> 
> - Tout code livré doit être testé de manière adéquate (cas passants et non passants)
> - Nous serons très vigilants sur le design, la qualité, et la lisibilité du code (et des commits)
> 
> Nous comprenons que chaque candidat a des contraintes de temps différentes, et nous valoriserons votre capacité à prioriser et à livrer un travail de qualité dans le temps imparti.
>

## Modalités de réalisation

> Pour réaliser ce kata : 
> - Tirez une branche depuis main
> - Réalisez vos développements sur cette branche
> - Quand vous êtes prêts à effectuer votre rendu, ouvrez une merge request vers main 
>
> ⚠️ L'ouverture de votre merge request déclenchera la revue de votre code !
> 
>⚠️ Cette merge request sert de support à la revue de code, **NE LA MERGEZ PAS !**
>


### Feature 1 : le compte bancaire

On souhaite proposer une fonctionnalité de compte bancaire. 

Ce dernier devra disposer : 

- D'un numéro de compte unique (format libre)
- D'un solde
- D'une fonctionnalité de dépôt d'argent
- D'une fonctionnalité de retrait d'argent

La règle métier suivante doit être implémentée : 

- Un retrait ne peut pas être effectué s'il représente plus d'argent qu'il n'y en a sur le compte

__          

### Feature 2 : le découvert

On souhaite proposer un système de découvert autorisé sur les comptes bancaires.

La règle métier suivante doit être implémentée : 

- Si un compte dispose d'une autorisation de découvert, alors un retrait qui serait supérieur au solde du compte est autorisé
si le solde final ne dépasse pas le montant de l'autorisation de découvert

__

### Feature 3 : le livret

On souhaite proposer un livret d'épargne.

Un livret d'épargne est un compte bancaire qui : 

- Dispose d'un plafond de dépôt : on ne peut déposer d'argent sur ce compte que dans la limite du plafond du compte (exemple : 22950€ sur un livret A)
- Ne peut pas avoir d'autorisation de découvert

__

### Feature 4 : le relevé de compte

On souhaite proposer une fonctionnalité de relevé mensuel (sur un mois glissant) des opérations sur le compte

Ce relevé devra faire apparaître : 

- Le type de compte (Livret ou Compte Courant)
- Le solde du compte à la date d'émission du relevé
- La liste des opérations ayant eu lieu sur le compte, triées par date, dans l'ordre antéchronologique



 






