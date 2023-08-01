from Boss import GoodBoss, BadBoss
def main():
    pass

julian = GoodBoss("Julian", "Positive", "Sociable", "Smiling")
bob = BadBoss("Bob", "negative", "crazy", "Spitting")

print("\nThe good boss is:")

julian.encourage()
julian.nurture_talent()

print("\nOn the other hand..\n\nThe bad boss is:")

bob.hoard_praise()
bob.yell()

print("\n Which boss is better??")


if __name__ == "__main__":
    main()
