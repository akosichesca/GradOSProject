#!/bin/bash
topp() (
  $* &
  pid="$!"
  trap ':' INT
  echo 'CPU  MEM'
  while sleep 0.01; do ps --no-headers -o '%cpu,%mem' -p "$pid"; done
  kill "$pid"
)

topp $*

