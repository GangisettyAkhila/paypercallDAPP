// src/utils/ellipseAddress.ts

const ellipseAddress = (address: string, width = 6): string => {
  if (!address) return ''
  return `${address.slice(0, width)}...${address.slice(-width)}`
}

export default ellipseAddress
