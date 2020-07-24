#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This would be O(n^2), the reason for that is that there are 2 operations in the code snippet and the runtime complexity will be higher based on the n value given.


b) This Would be O(n), the reason for that is, on this code snippet, the runtime complexity will only increase based on the n value given.


c) This would be O(2^n), the reason is that there are 2 operations and the operation recursion increases to the power of n given in the operation.

## Exercise II
- so we have the components which are: the building with n-floors and an x amount of eggs, our goal is to minimize the broken eggs if dropped from a certain floor.
- first we need a threshold of what is considered a safe height and a dangerous height.
- if a building only has 1 story, and the eggs are thrown from there, i assume that the eggs would not break...also under the assumption that these eggs are raw. if the building has more than one story, if the eggs are thrown from a floor above our first floor they will break.

# pseudo code:
```
save_the_eggs(building=n):
    eggs = random.amount()
    saved = 0
    broken = 0
    # check if the building is more than one story
    # if that is the case all the eggs are saved
    if building == 1:
        eggs -= eggs # all the eggs are thrwon from there   
        saved += eggs                #and all the eggs                          #aresaved!
    # now if the eggs are thrown from a floor above the #first floor, they will break
    for n in range(building):
        if n > n:
        broken += eggs
        eggs -= eggs

         


```
- The Runtime complexity of this problem will be O(n)
because it would only grow based on the n numbers of stories of the given building.


