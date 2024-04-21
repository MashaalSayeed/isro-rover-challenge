// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from interfaces:srv/AddObjectSrv.idl
// generated code does not contain a copyright notice
#include "interfaces/srv/detail/add_object_srv__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "interfaces/srv/detail/add_object_srv__struct.h"
#include "interfaces/srv/detail/add_object_srv__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "geometry_msgs/msg/detail/pose__functions.h"  // pose

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_interfaces
size_t get_serialized_size_geometry_msgs__msg__Pose(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_interfaces
size_t max_serialized_size_geometry_msgs__msg__Pose(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, geometry_msgs, msg, Pose)();


using _AddObjectSrv_Request__ros_msg_type = interfaces__srv__AddObjectSrv_Request;

static bool _AddObjectSrv_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AddObjectSrv_Request__ros_msg_type * ros_message = static_cast<const _AddObjectSrv_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: pose
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, geometry_msgs, msg, Pose
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->pose, cdr))
    {
      return false;
    }
  }

  // Field name: tag
  {
    cdr << ros_message->tag;
  }

  return true;
}

static bool _AddObjectSrv_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AddObjectSrv_Request__ros_msg_type * ros_message = static_cast<_AddObjectSrv_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: pose
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, geometry_msgs, msg, Pose
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->pose))
    {
      return false;
    }
  }

  // Field name: tag
  {
    cdr >> ros_message->tag;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_interfaces
size_t get_serialized_size_interfaces__srv__AddObjectSrv_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AddObjectSrv_Request__ros_msg_type * ros_message = static_cast<const _AddObjectSrv_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name pose

  current_alignment += get_serialized_size_geometry_msgs__msg__Pose(
    &(ros_message->pose), current_alignment);
  // field.name tag
  {
    size_t item_size = sizeof(ros_message->tag);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AddObjectSrv_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_interfaces__srv__AddObjectSrv_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_interfaces
size_t max_serialized_size_interfaces__srv__AddObjectSrv_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: pose
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_geometry_msgs__msg__Pose(
        full_bounded, current_alignment);
    }
  }
  // member: tag
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _AddObjectSrv_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_interfaces__srv__AddObjectSrv_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_AddObjectSrv_Request = {
  "interfaces::srv",
  "AddObjectSrv_Request",
  _AddObjectSrv_Request__cdr_serialize,
  _AddObjectSrv_Request__cdr_deserialize,
  _AddObjectSrv_Request__get_serialized_size,
  _AddObjectSrv_Request__max_serialized_size
};

static rosidl_message_type_support_t _AddObjectSrv_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AddObjectSrv_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, interfaces, srv, AddObjectSrv_Request)() {
  return &_AddObjectSrv_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "interfaces/srv/detail/add_object_srv__struct.h"
// already included above
// #include "interfaces/srv/detail/add_object_srv__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _AddObjectSrv_Response__ros_msg_type = interfaces__srv__AddObjectSrv_Response;

static bool _AddObjectSrv_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AddObjectSrv_Response__ros_msg_type * ros_message = static_cast<const _AddObjectSrv_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    cdr << ros_message->success;
  }

  return true;
}

static bool _AddObjectSrv_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AddObjectSrv_Response__ros_msg_type * ros_message = static_cast<_AddObjectSrv_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    cdr >> ros_message->success;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_interfaces
size_t get_serialized_size_interfaces__srv__AddObjectSrv_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AddObjectSrv_Response__ros_msg_type * ros_message = static_cast<const _AddObjectSrv_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name success
  {
    size_t item_size = sizeof(ros_message->success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AddObjectSrv_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_interfaces__srv__AddObjectSrv_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_interfaces
size_t max_serialized_size_interfaces__srv__AddObjectSrv_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: success
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _AddObjectSrv_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_interfaces__srv__AddObjectSrv_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_AddObjectSrv_Response = {
  "interfaces::srv",
  "AddObjectSrv_Response",
  _AddObjectSrv_Response__cdr_serialize,
  _AddObjectSrv_Response__cdr_deserialize,
  _AddObjectSrv_Response__get_serialized_size,
  _AddObjectSrv_Response__max_serialized_size
};

static rosidl_message_type_support_t _AddObjectSrv_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AddObjectSrv_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, interfaces, srv, AddObjectSrv_Response)() {
  return &_AddObjectSrv_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "interfaces/srv/add_object_srv.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t AddObjectSrv__callbacks = {
  "interfaces::srv",
  "AddObjectSrv",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, interfaces, srv, AddObjectSrv_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, interfaces, srv, AddObjectSrv_Response)(),
};

static rosidl_service_type_support_t AddObjectSrv__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &AddObjectSrv__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, interfaces, srv, AddObjectSrv)() {
  return &AddObjectSrv__handle;
}

#if defined(__cplusplus)
}
#endif