class GlobalCounter {

    constructor() {
        if (GlobalCounter.instance) {
            return GlobalCounter.instance
        }
        GlobalCounter.instance = this
        this.counters = {}
    }

    static resetInstance() {
        GlobalCounter.instance = undefined
    }

    increment(counterName) {
        if (!this.counters[counterName]) {
            this.counters[counterName] = 1
            return
        }
        this.counters[counterName] += 1
    }

    decrement(counterName) {
        if (!this.counters[counterName]) {
            this.counters[counterName] = -1
            return
        }
        this.counters[counterName] -= 1
    }

    getValue(counterName) {
        return this.counters[counterName] ?? 0
    }

    reset(counterName) {
        if (counterName) {
            this.counters[counterName] = 0
            return
        }

        for (let counter in this.counters) {
            this.counters[counter] = 0
        }
    }

    listCounters() {
        return this.counters
    }

}

module.exports = GlobalCounter