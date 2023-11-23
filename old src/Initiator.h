#pragma once
#ifndef INITIATOR_H
#define INITIATOR_H

#include <systemc.h>
#include "tlm.h"
#include "tlm_utils/simple_initiator_socket.h"
#include "Target.h"

using namespace tlm;

struct Initiator : sc_core::sc_module {
    tlm_utils::simple_initiator_socket<Initiator> init_socket;

    void sendDataThread();

    SC_CTOR(Initiator) : init_socket("init_socket") {
        SC_THREAD(sendDataThread);
    }
};

#endif  // INITIATOR_H

