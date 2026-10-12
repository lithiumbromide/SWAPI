---
title: "Overview of Macro Features"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Overview_of_Macro_Features.htm"
---

# Overview of Macro Features

Macro features are application-defined features that users can add to a SOLIDWORKS model. The effect of a macro feature on the model is defined by programs that you, or a third-party, develop.

Macro features use one of two techniques to specify their intended behavior. They can be associated either with functions:

- contained within a SOLIDWORKS [VBA macro file (*.swp)](VBA_Macro_Files.htm).

  - or -
- exposed by a [COM server DLL or executable](Exposed_COM_DLL_or_Executable.htm).

**NOTE**: You cannot record or write macro features using SOLIDWORKS .NET macros.

You must write macro feature functions to define your macro feature.

| Macro feature function | VBA | COM | Comment |
| --- | --- | --- | --- |
| Edit definition | Required | Required | Called whenever the user edits the macro feature's definition. |
| Rebuild | Required | Required | Called whenever the macro feature rebuilds. |
| Security | Optional | Required | Allows you to specify whether instances of the macro feature can be edited, suppressed, or deleted from the model. |

The names of the VBA macro feature functions must begin with swm. For example, you could name the functions swmEdit, swmRebuild, and swmSecurity.

Users must be able to run the program that creates the macro feature whenever they want to add one to a model.

The [IMacroFeatureData Interface](MacroFeatureData_Interface.htm) supports macro features.
