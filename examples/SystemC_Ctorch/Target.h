#pragma once
#ifndef TARGET_H
#define TARGET_H

#include <systemc.h>
#include "tlm.h"
#include "tlm_utils/simple_target_socket.h"
#include <vector>
#include "json/json.hpp"
#include <torch/script.h>
#include <torch/torch.h>
#include <torch/nn.h>
#include <torch/optim.h>
#include <torch/data/example.h>
#include <torch/csrc/jit/serialization/import.h>
#include <opencv2/opencv.hpp>
#include <ctime>

using namespace tlm;
using namespace torch;
using namespace std;
using namespace sc_core;
using namespace tlm_utils;

struct Target : sc_module
{
    simple_target_socket<Target> target_socket;
    vector<float> flattened_array;

    SC_CTOR(Target);

    void b_transport(tlm_generic_payload &payload, sc_time &tLOCAL);
};

#endif // TARGET_H