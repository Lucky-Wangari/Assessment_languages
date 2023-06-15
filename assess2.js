// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.
class Story {
    constructor(title, content, moralLesson, ageGroup, stories) {
      this.title = title;
      this.content = content;
      this.moralLesson = moralLesson;
      this.ageGroup = ageGroup;
      this.stories = stories;
    }
    addStory() {
        this.stories.push(this.content);
      }
      tellStory(storyTitle) {
        for (let story of this.stories) {
          if (story.title === storyTitle) {
            return "Story found";
          }
        }
        return "Story not found.";
      }
    
  }
  
    
    

  
  class Translate {
    constructor(source, Language) {
      this.source = source;
      this.Language = Language;
    }
  
    translate() {
      return "Translated text";
    }
  }
  
//Create a class called Product with attributes for name, price, and quantity.
//Implement a method to calculate the total value of the product (price * quantity).
//Create multiple objects of the Product class and calculate their total values.

class Product {
    constructor(name, price, quantity) {
      this.name = name;
      this.price = price;
      this.quantity = quantity;
    }
  
    totalValue() {
      return this.price * this.quantity;
    }
  }
