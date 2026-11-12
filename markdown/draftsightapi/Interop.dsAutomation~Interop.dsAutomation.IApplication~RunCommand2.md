---
title: "RunCommand2 Method (IApplication)"
project: ""
interface: "IApplication"
member: "RunCommand2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand2.html"
---

# RunCommand2 Method (IApplication)

Runs the specified command.

## Syntax

### Visual Basic

```vb
Function RunCommand2( _
   ByVal CommandString As System.String, _
   ByVal ParameterStrArray As System.Object, _
   ByVal ParameterTypeLongArray As System.Object, _
   ByVal HideCommandTitle As System.Boolean _
) As dsRunCommandError_e
```

### C#

```csharp
dsRunCommandError_e RunCommand2(
   System.string CommandString,
   System.object ParameterStrArray,
   System.object ParameterTypeLongArray,
   System.bool HideCommandTitle
)
```

### JScript

```
function RunCommand2(
   CommandString : System.String,
   ParameterStrArray : System.Object,
   ParameterTypeLongArray : System.Object,
   HideCommandTitle : System.boolean
) : dsRunCommandError_e;
```

### Managed Extensions for C++

```
dsRunCommandError_e RunCommand2(
   System.string* CommandString,
   System.Object* ParameterStrArray,
   System.Object* ParameterTypeLongArray,
   System.bool HideCommandTitle
)
```

### C++/CLI

```cpp
dsRunCommandError_e RunCommand2(
   System.String^ CommandString,
   System.Object^ ParameterStrArray,
   System.Object^ ParameterTypeLongArray,
   System.bool HideCommandTitle
)
```

### Parameters

- `CommandString`: Name of command to run (see **Remarks**)
- `ParameterStrArray`: Array of parameters to execute with the command
- `ParameterTypeLongArray`: Array of ParameterStrArray types as defined by [dsResType_e](Interop.dsAutomation~Interop.dsAutomation.dsResType_e.html); the size of this array much match the size of ParameterStrArray
- `HideCommandTitle`: True to hide the command in the command window, false to show the command in the command window

### Return Value

Status of running the command as defined in [dsRunCommandError_e](Interop.dsAutomation~interop.dsAutomation.dsRunCommandError_e.html)

## Examples

Create a C++ program in Visual Studio using the C++ snippet below, substituting `your_pdf` with the full path to a PDF file on your computer.

=======================================================================

C++ snippet attaches and detaches `your_pdf`

=============================================================================

dsCommandMessage_ptr commandline;

application->**GetCommandMessage**(&commandline);

dsRunCommandError_e error = dsRunCommand_InvalidCommand;

dsStringArray parameters;

dsLongArray parametersLong;

dsString strFile = L"`your_pdf`";

dsResType_e type = dsResType_String;

parameters.add( strFile );

parametersLong.add( type );

application->**RunCommand2**( L"_ATTACHPDF", parameters, parametersLong, true, &error );

commandline->**PrintLine**( error != dsRunCommand_Succeeded ? L"Run command failed" : L"Run command passed!" );

dsDocument_ptr document;

application->**GetActiveDocument**( &document );

dsLongArray ExternalDefinitionTypeLongArray;

dsObjectPtrArray ExternalDefinitionsArray;

document->**GetImmediateChildReferences**( &ExternalDefinitionTypeLongArray, &ExternalDefinitionsArray );

dsModel_ptr dsModel;

document->**GetModel**( &dsModel );

dsSketchManager_ptr sketchManager;

dsModel->**GetSketchManager**( &sketchManager );

dsPdfDefinition_c* pdfDefinition = ( dsPdfDefinition_c* )ExternalDefinitionsArray[ 0 ];

bool bRet;

sketchManager->**DetachPdfDefinition**( pdfDefinition, &bRet );

commandline->**PrintLine**( bRet ? L"Passed to detach Pdf" : L"Failed to detach PDF" );

## Examples

[Insert Splines (VBA)](Insert_Splines_Example_VBA.htm)
[Insert Splines (VB.NET)](Insert_Splines_Example_VBNET.htm)
[Insert Splines (C#)](Insert_Splines_Example_CSharp.htm)

## Remarks

Depending on the programming language that you use, either:

- append **\n** to the command
  - or -

- include **& Chr(10)** after the command

  These control strings emulate a user pressing the Enter key in DraftSight. The number of control strings should correspond to the number of times a user is required to press the Enter key for the command in DraftSight.

For example:

| To delete all entities in a drawing in this programming language... | Call... |
| --- | --- |
| C# | int state; state = (int)dsApp. RunCommand (" DELETE ALL\n\n ", false); |
| VB.NET | Dim state as Integer; state = dsApp. RunCommand (" DELETE ALL" & Chr(10) & Chr(10) , False) |
| VBA | Dim state as Long; state = dsApp. RunCommand (" DELETE ALL" & Chr(10) & Chr(10) , False) |

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AbortRunningCommand Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AbortRunningCommand.html)
[IApplication::CreateCommand4 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand4.html)
[IApplication::GetRunningCommand Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRunningCommand.html)
[ICommand Interface](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)
[_ICommandEvents_ExecuteNotifyEventHandler Delegate](Interop.dsAutomation~Interop.dsAutomation._ICommandEvents_ExecuteNotifyEventHandler.html)
[ICommandMessage::GetLastError Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~GetLastError.html)
[ICommand::LastError Property ()](Interop.dsAutomation~Interop.dsAutomation.ICommand~LastError.html)
[_IApplicationEvents_CommandCancelNotifyEventHandler Delegate](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandCancelNotifyEventHandler.html)
[_IApplicationEvents_CommandPostNotifyEventHandler Delegate](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPostNotifyEventHandler.html)
[_IApplicationEvents_CommandPreNotifyEventHandler Delegate](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPreNotifyEventHandler.html)

## Availability

DraftSight 2024 SP02
