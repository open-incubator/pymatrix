```
    ___               _   __      ___    __  ___  __     ( )       
  //   ) ) //   / / // ) )  ) ) //   ) )  / /   //  ) ) / / \\ / / 
 //___/ / ((___/ / // / /  / / //   / /  / /   //      / /   \/ /  
//            / / // / /  / / ((___( (  / /   //      / /    / /\
```

🔌 The world in a computer, virtual representation of the reality

![Demo](https://s8.gifyu.com/images/demo89ed580835b4b321.gif)

## Why
I was studying a text from Bergson about consciousness in my philosophy lesson when the guy in front of me could not believe that we could be inside a computer simulation. It was so unbelievable for him that even the arguments of the teacher could not convince him. That's why I decided to prove that everything can be a simulation. I created this small program with basic rules to "virtualize" our world.
I also decided to make it open-source for this [Hacktoberfest month](https://hacktoberfest.digitalocean.com/) to share how simple it would be to create a basic simulation of our lives. If a 17 years old programmer achieved this in a few days, we can ask ourselves if someone could achieve the entire simulation of our world with all its complexity and all its rules in 2000 years.

## How it works
At the beginning of the program, the size of the world is defined. The size also defines the limit of people the world can handle. If the limit is reached, the world crash. The first number of people is also defined (these people will spawn at the beginning of the program before everything starts). As in the real world, everybody receives an ID at birth, this ID allows us to track what people do.
This simulation has three main concepts : **events**,  **relationships** and **life cycle**

### Events
This world has four events that can be triggered by someone:

* Go to work (`W`)
* Go shopping (`S`)
* Go back home (`H`)
* Give birth to someone (`B`)

The program randomly decides on who should be triggered the event and when it should be. Humans think they make their own choices but in fact the program instills in them the choices they had to make.

### Relationships
Every time somebody is at the same place as someone else, they create a link between them: a relationship. There are three types of relationships:
1. Acquaintance 
2. Friend
3. Partner

A few things to know about the partner type:
* You can have only one partner
* Once you have a partner you can give birth to someone

### Life cycle
The life cycle begins when someone is born. Since this event, this person is one year older every 0.1 seconds (I know that's fast but it would be boring if we had to wait 60 years to see people die, I would be probably dead when the first person of the matrix will be dead... So yes I prefer it to be fast). Once somebody is 60 years old, the chance to die is 60% (you can not die until you are 60 years old). Then this chance increases every year, so every 0.1 seconds, somebody has 1% more.

## Read the matrix

I agree with you, at first glance, the output of the matrix is very strange. Let me explain this to you.
Every line of the matrix is composed of:
```
Coords.X:Coords.Y:ID:Event
```

So you can see who makes what and where.

For example :
```
10:20:1:W
  |   | |
  |   | |_______________________________________________ Go to work
  |   |___________________ The person who has the ID 1
  |
The place where he is
```

You could ask me, why did you do that? That's stupid you could just write :
```
The person who has the ID 1 goes to work on X:10; Y:20
```

That's right but at the speed of the matrix, you won't be able to read anything if it were not just letters and numbers. At this speed, I challenge you to read one word.

## In the future
Since this project is open-source, here is what we could create with the matrix:

* Transform it into a webhook server so we could create an interpreter to act on the matrix. Change it live, for example: give birth to someone or make somebody else die.
* Create a graphical representation of the matrix, just a few points on a "squared sheet" with their id on top of them would be a good beginning.