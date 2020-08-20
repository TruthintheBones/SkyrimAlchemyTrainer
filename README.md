# SkyrimAlchemyTrainer
Given CSV-based ingredient inventory, prints brewing instructions that will discover potion effects at a high rate.

This program is intended to reduce the tedium of discovering ingredient effects in TES V: Skyrim. Chronic restarters, rejoice!

The accompanying .CSV file saves your discovery progress and inventory. A row in the CSV file looks like this:

        Abecean_Longfin,0,Weakness_to_Frost,0,Fortify_Sneak,0,Weakness_to_Poison,0,Fortify_Restoration,0
        
...which follows the scheme...

        Ingredient_name,number_in_inventory,effect_1_name,is_effect_1_known?,effect_2_name,is_effect_2_known?.... etc.

Before running this program, manually update the CSV to reflect the current status of your Skyrim character's alchemy situation. In particular, update the inventory column to reflect your character's inventory of ingredients. This program is really designed for fresh characters, but if your character has done alchemy before, you may also manually record which effects of which ingredients your character already knows by changing the corresponding 0 to a 1, but that sounds MISERABLE, and is not encouraged. Instead, just allow the program to assume your character knows no ingredient effects. This will result in some wasted ingredients, of course, but the program will quickly catch up to your current progress.

After setting up, saving, and closing the CSV, run the program. It will generate a list of potion brewing instructions. Brew potions in this order to discover a large number of effects.

Once it's not possible to learn more effects, you will have the option of continuing to brew potions. This will produce a list of instructions that yields valuable potions until you can't produce any more potions.

When you are finished, you will have the option of automatically updating the .CSV to match your discovery progress and inventory. (Only do this if you carried out the program's instructions)

Before your next session, remember to update the inventory column of your CSV again.

TIPS & NOTES
1. This works best when you've saved up a large stockpile of ingredients. Working in smaller batches produces worse results and requires more manual fussing with the .CSV.
2. This program only considers potions with 3 ingredients. 3-ingredient potions tend to discover ingredients more efficiently and convert your inventory of ingredients into a set of potions that are worth more gold/experience overall. This is not necessarily the case for any given ingredient inventory, but this program ignores those exceptions.
3. This program might not always result in the true maximum possible discovered effects. What it literally does is repeatedly determine the single potion that discovers the most effects. In funny cases, this might not truly result in the maximum number of effects discovered in the session overall. What if, for example, consuming some ingredients to discover 5 effects prevents you from discovering 3 effects on two occasions down the line?
4. This program works with the base game and all DLCs but makes no special consideration for any mod.
