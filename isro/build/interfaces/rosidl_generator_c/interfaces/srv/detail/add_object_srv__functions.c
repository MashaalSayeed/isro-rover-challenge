// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:srv/AddObjectSrv.idl
// generated code does not contain a copyright notice
#include "interfaces/srv/detail/add_object_srv__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
interfaces__srv__AddObjectSrv_Request__init(interfaces__srv__AddObjectSrv_Request * msg)
{
  if (!msg) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__init(&msg->pose)) {
    interfaces__srv__AddObjectSrv_Request__fini(msg);
    return false;
  }
  // tag
  return true;
}

void
interfaces__srv__AddObjectSrv_Request__fini(interfaces__srv__AddObjectSrv_Request * msg)
{
  if (!msg) {
    return;
  }
  // pose
  geometry_msgs__msg__Pose__fini(&msg->pose);
  // tag
}

bool
interfaces__srv__AddObjectSrv_Request__are_equal(const interfaces__srv__AddObjectSrv_Request * lhs, const interfaces__srv__AddObjectSrv_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  // tag
  if (lhs->tag != rhs->tag) {
    return false;
  }
  return true;
}

bool
interfaces__srv__AddObjectSrv_Request__copy(
  const interfaces__srv__AddObjectSrv_Request * input,
  interfaces__srv__AddObjectSrv_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  // tag
  output->tag = input->tag;
  return true;
}

interfaces__srv__AddObjectSrv_Request *
interfaces__srv__AddObjectSrv_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__srv__AddObjectSrv_Request * msg = (interfaces__srv__AddObjectSrv_Request *)allocator.allocate(sizeof(interfaces__srv__AddObjectSrv_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__srv__AddObjectSrv_Request));
  bool success = interfaces__srv__AddObjectSrv_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interfaces__srv__AddObjectSrv_Request__destroy(interfaces__srv__AddObjectSrv_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interfaces__srv__AddObjectSrv_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interfaces__srv__AddObjectSrv_Request__Sequence__init(interfaces__srv__AddObjectSrv_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__srv__AddObjectSrv_Request * data = NULL;

  if (size) {
    data = (interfaces__srv__AddObjectSrv_Request *)allocator.zero_allocate(size, sizeof(interfaces__srv__AddObjectSrv_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__srv__AddObjectSrv_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__srv__AddObjectSrv_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__srv__AddObjectSrv_Request__Sequence__fini(interfaces__srv__AddObjectSrv_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__srv__AddObjectSrv_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__srv__AddObjectSrv_Request__Sequence *
interfaces__srv__AddObjectSrv_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__srv__AddObjectSrv_Request__Sequence * array = (interfaces__srv__AddObjectSrv_Request__Sequence *)allocator.allocate(sizeof(interfaces__srv__AddObjectSrv_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interfaces__srv__AddObjectSrv_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interfaces__srv__AddObjectSrv_Request__Sequence__destroy(interfaces__srv__AddObjectSrv_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interfaces__srv__AddObjectSrv_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interfaces__srv__AddObjectSrv_Request__Sequence__are_equal(const interfaces__srv__AddObjectSrv_Request__Sequence * lhs, const interfaces__srv__AddObjectSrv_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__srv__AddObjectSrv_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__srv__AddObjectSrv_Request__Sequence__copy(
  const interfaces__srv__AddObjectSrv_Request__Sequence * input,
  interfaces__srv__AddObjectSrv_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__srv__AddObjectSrv_Request);
    interfaces__srv__AddObjectSrv_Request * data =
      (interfaces__srv__AddObjectSrv_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__srv__AddObjectSrv_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__srv__AddObjectSrv_Request__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__srv__AddObjectSrv_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
interfaces__srv__AddObjectSrv_Response__init(interfaces__srv__AddObjectSrv_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
interfaces__srv__AddObjectSrv_Response__fini(interfaces__srv__AddObjectSrv_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
interfaces__srv__AddObjectSrv_Response__are_equal(const interfaces__srv__AddObjectSrv_Response * lhs, const interfaces__srv__AddObjectSrv_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
interfaces__srv__AddObjectSrv_Response__copy(
  const interfaces__srv__AddObjectSrv_Response * input,
  interfaces__srv__AddObjectSrv_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

interfaces__srv__AddObjectSrv_Response *
interfaces__srv__AddObjectSrv_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__srv__AddObjectSrv_Response * msg = (interfaces__srv__AddObjectSrv_Response *)allocator.allocate(sizeof(interfaces__srv__AddObjectSrv_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__srv__AddObjectSrv_Response));
  bool success = interfaces__srv__AddObjectSrv_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interfaces__srv__AddObjectSrv_Response__destroy(interfaces__srv__AddObjectSrv_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interfaces__srv__AddObjectSrv_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interfaces__srv__AddObjectSrv_Response__Sequence__init(interfaces__srv__AddObjectSrv_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__srv__AddObjectSrv_Response * data = NULL;

  if (size) {
    data = (interfaces__srv__AddObjectSrv_Response *)allocator.zero_allocate(size, sizeof(interfaces__srv__AddObjectSrv_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__srv__AddObjectSrv_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__srv__AddObjectSrv_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__srv__AddObjectSrv_Response__Sequence__fini(interfaces__srv__AddObjectSrv_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__srv__AddObjectSrv_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__srv__AddObjectSrv_Response__Sequence *
interfaces__srv__AddObjectSrv_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__srv__AddObjectSrv_Response__Sequence * array = (interfaces__srv__AddObjectSrv_Response__Sequence *)allocator.allocate(sizeof(interfaces__srv__AddObjectSrv_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interfaces__srv__AddObjectSrv_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interfaces__srv__AddObjectSrv_Response__Sequence__destroy(interfaces__srv__AddObjectSrv_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interfaces__srv__AddObjectSrv_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interfaces__srv__AddObjectSrv_Response__Sequence__are_equal(const interfaces__srv__AddObjectSrv_Response__Sequence * lhs, const interfaces__srv__AddObjectSrv_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__srv__AddObjectSrv_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__srv__AddObjectSrv_Response__Sequence__copy(
  const interfaces__srv__AddObjectSrv_Response__Sequence * input,
  interfaces__srv__AddObjectSrv_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__srv__AddObjectSrv_Response);
    interfaces__srv__AddObjectSrv_Response * data =
      (interfaces__srv__AddObjectSrv_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__srv__AddObjectSrv_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          interfaces__srv__AddObjectSrv_Response__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__srv__AddObjectSrv_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
