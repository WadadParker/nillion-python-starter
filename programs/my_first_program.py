from nada_dsl import *
import random


def nada_prisoners_dilemma_fixed_money():
  
  # This program simulates the prisoner's dilemma with a fixed initial amount 
  # and secure multi-party computation.

  party1 = Party(name="Party1")
  party2 = Party(name="Party2")

  fixed_money = SecretInteger(random(1000))

  choice_party1 = SecretInteger(Input(name="choice", party=party1))
  choice_party2 = SecretInteger(Input(name="choice", party=party2))

  # Helper function to calculate each party's payout based on choices
  def calculate_payout(choice1, choice2, total):
    if choice1 == 1 and choice2 == 1:
      return total // 2
    elif choice1 == 0 or choice2 == 0:
      return total * (choice1 == choice2) 
    else:
      return 0

  # Calculate payouts for each party using a secure function
  payout_party1 = calculate_payout(choice_party1, choice_party2, fixed_money)
  payout_party2 = calculate_payout(choice_party2, choice_party1, fixed_money)

  # Each party only learns their own payout (revealed secretly)
  return [
      Output(payout_party1, "payout", party1),
      Output(payout_party2, "payout", party2),
  ]
