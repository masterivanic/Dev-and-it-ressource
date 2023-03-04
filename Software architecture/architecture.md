# Software architecture foundations

Architect : Designer of complete systems

Drawback of traditional  architect
    1.  Big and complex design
        + Code is written after design
        + Doesn't capture the user's needs
        + Doesn't allow for learning

    2. Lack of flexibility
        + Painful bureaucratic processes
        + Not following desing
        + Random improvisation
    
    3. Slow development process
        + Centralized architect-making decisions
        + Wasted time and money

Agile Architecture (Servant leader) have roles such as: Teaching, Coaching and coordinate
Main design responsibility:assure coherence across system by Reviews work, make suggestions, helps refine process

Design patterns provide sets of optimal solutions
Architecture is the interaction of design patterns

Improve Technical Understanding:
    + Read code
    + Study open source projects
    + Form a study group

## Conway's law:
 > Any organnization that designs a system... will inevitably produce a design whose structure is a copy of orgranization's communication structure.

Big UP-Front Designs (BUFD) | Agile Incremental Design
    User interface          |    Customer
    Business logic          |    Stories
    Database                |    Technology

Domain-Driven Design (DDD)
The structure of your code should map to the structure of the problem domain.
DDD focuses on creating software systems that match the problem domain. The system is modularized, making it easier to build and modify  

Ubiquitous Language in DD
Speak the language of your customers.
The same word can mean different things under
different contexts. This is okay

Agents enhance communication between subsystems of a domain of the business
An agent is a course-grained implementation, and the details of an agent's work are hidden inside of it.

Agents technologies:
    + Messaging - simplify communication across a network

    + Caching - store data locally in memory instead of in a slower and harder-to-access database

    + Logging - track your programm does as it works

    + Monitoring - observe how your program uses system resources as it works

Think about how your agents communicate it could be xml, json 

Optimizations:
    + Explore open-source and free-software solutions
    + Avoid being forced into a specific ecosystem

Categories of Architecture:
    + System and EA (Entreprise Architecture)
    + Design patterns

Broad Architecture Patterns:
    + Monoliths
    + Microkernel(plugin) architecture
    + Message based architectures
    + Microservices and miniservices
    + Reactive and choreograph systems

