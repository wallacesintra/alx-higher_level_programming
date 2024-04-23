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
        const completed_tasks = tasks.filter((task) => task.completed === true);
        // console.log(completed_tasks.length);

        const completed_tasks_by_user = {};
        for (const task of completed_tasks) {
            if (task.userId in completed_tasks_by_user) {
                completed_tasks_by_user[task.userId]++;
            } else {
                completed_tasks_by_user[task.userId] = 1;
            }
        }
        console.log(completed_tasks_by_user);
    }
});
