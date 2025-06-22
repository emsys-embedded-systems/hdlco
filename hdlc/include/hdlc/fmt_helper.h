#pragma once

#include <fmt/ostream.h>

#include "hdlc/stream_helper.h"

template <> struct fmt::formatter<hdlc::Frame> : ostream_formatter {};
template <> struct fmt::formatter<hdlc::Frame::Type> : ostream_formatter {};
template <> struct fmt::formatter<hdlc::StatusError> : ostream_formatter {};
template <> struct fmt::formatter<hdlc::ConnectionStatus> : ostream_formatter {};
