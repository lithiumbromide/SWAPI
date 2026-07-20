---
title: "Programming Tasks"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/Tasks.htm"
---

# Programming Tasks

In
SOLIDWORKS PDM Professional 2009 and earlier, add-ins work only on single client machines:

- A change-state hook calls the add-in on the machine where the change state command
  is executed.

- or -

- A menu
  command executes the add-in on the computer where the menu command is selected.

Although this is often desirable, there are times when you want to execute the add-in on different machines. SOLIDWORKS PDM
Professional and later allow you to program tasks to execute add-ins on other
machines.

A task consists of:

- Add-in to execute.
- Dialog or form to show when the task is launched.
- User credentials to use to execute the add-in.
- Computers on which to execute the add-in.
- Optional scheduling of the add-in.
- Credentials of users who have permission to run the add-in.
- Error and success notifications.

You can read more about
the task execution system in the SOLIDWORKS PDM Professional Help.

To program your own task:

1. Write an add-in DLL that supports
  task execution.
2. Add the add-in
  to the vault using the Administration tool.
3. Enable execution of the add-in on one or more servers by
  selecting the Task Host Configuration command from the context-sensitive menu on the SOLIDWORKS PDM Professional icon in the task bar navigation area
  (system tray).
4. Right-click the tasks node in the Administration tool and select

  New Task

  from the menu.
5. Select your add-in
  in the task wizard.
6. Select other options in the task wizard.

The task is executed in one of the following ways:

- A task definition spawns task instances
  according to a defined schedule.
- A workflow change
  state action executes the task.
- Start the Administration tool, expland

  Tasks

  ,
  double-click

  Task List

  , and click

  Add Task

  .
- Right-click a file vault view and select the task on the
  context-sensitive menu.

### Using the Standard Task Add-in

You do not need to program your own task add-in if you only need to open files in SOLIDWORKS and execute scripts on them. To do
that, use the[standard task add-in](StandardTaskAddIn.htm)that is shipped with SOLIDWORKS PDM Professional.

### Code
Samples

- [Task Add-in Sample (VB.NET)](TaskSample.htm)
- [Task Add-in Sample (C#)](TaskSample_CSharp.htm)

### Interfaces

- [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html)
- [IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
- [IEdmTaskProperties](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)

### Structures and Constants

- [EdmTaskFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskFlag.html)
- [EdmTaskMenuCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd.html)
- [EdmTaskSel](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel.html)
- [EdmTaskSetupPage](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSetupPage.html)
- [EdmTaskStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskStatus.html)
