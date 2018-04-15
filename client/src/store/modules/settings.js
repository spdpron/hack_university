import shop from '../../api/shop'

// initial state
const state = {
  parentLinks: [], // string array
  childLinks: [], // object array. Each link has its 'id'.
  crawlFields: [] // object array. They are not nested. Each field has its 'id'.
  // Object property 'fields' is an array of ids
}

// getters
const getters = {
  parentLinks: state => state.parentLinks,

  childLinks: state => state.childLinks,
  
  crawlField: state => fieldId => {
    for (let i = 0; i < state.crawlFields.length; i++) {
      if (state.crawlFields[i].id === fieldId) {
        return state.crawlFields[i]
      }
    }
    return null
  },

  childLink: state => linkId => {
    for (let i = 0; i < state.childLinks.length; i++) {
      if (state.childLinks[i].id === linkId) {
        return state.childLinks[i]
      }
    }
    return null
  },

  _composeChildFieldsAndLinks: state => fieldId => {W
    let parentField = this.crawlField(fieldId)
    if (parentField === null)
      return []

    let copiedParent = JSON.parse(JSON.stringify(parentField))
    for (let i = 0; i < copiedParent.fields.length; i++) {
      copiedParent.fields[i] = this._composeChildFieldsAndLinks(copiedParent.fields[i])
    }
    for (let i = 0; i < copiedParent.fields.length; i++) {
      copiedParent.fields[i] = this._composeChildFieldsAndLinks(copiedParent.fields[i])
    }
    return copiedParent
  },

  nestedCrawlFields: (state, getters) => {
    var targetArray = []
    for (let i = 0; i < state.crawlFields.length; i++) {
      targetArray.push(this._composeChildFieldsAndLinks(state.crawlFields[i].id))
    }
    return targetArray
  }
}

// mutations
const mutations = {
  addChildLink (state, { parentId }) {
    state.childLinks.push({
      name: '',
      xPath: '',
      cssClass: '',
      id: '',
      _id: Date.now()
    })
  },

  incrementItemQuantity (state, { id }) {
    const cartItem = state.added.find(item => item.id === id)
    cartItem.quantity++
  },

  setCartItems (state, { items }) {
    state.added = items
  },

  setCheckoutStatus (state, status) {
    state.checkoutStatus = status
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}