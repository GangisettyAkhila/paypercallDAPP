// utils/CallService.ts
// Utility to initiate a Pay-Per-Call payment transaction (placeholder logic)

import algosdk from 'algosdk'

export const initiateCallPayment = async (
  sender: string,
  receiver: string,
  amountAlgo: number,
  algodClient: algosdk.Algodv2
) => {
  try {
    const params = await algodClient.getTransactionParams().do()

    const txn = algosdk.makePaymentTxnWithSuggestedParamsFromObject({
      from: sender,
      to: receiver,
      amount: algosdk.algosToMicroalgos(amountAlgo),
      suggestedParams: params,
    })

    return txn
  } catch (err) {
    console.error('Error initiating call payment:', err)
    throw err
  }
}
