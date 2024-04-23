#!/usr/bin/node

/**
 * display the number of completed tasks
 */

const req = require('request');
const url = process.argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.filter((task) => task.completed === true);
    // console.log(completed_tasks.length);

    const completedTaskByUser = {};
    for (const task of completedTasks) {
      if (task.userId in completedTaskByUser) {
        completedTaskByUser[task.userId]++;
      } else {
        completedTaskByUser[task.userId] = 1;
      }
    }
    console.log(completedTaskByUser);
  }
});
