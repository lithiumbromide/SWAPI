---
title: "RecordLine Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RecordLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.html"
---

# RecordLine Method (ISldWorks)

Adds a line of code to a VBA macro and the SOLIDWORKS journal file.

## Syntax

### Visual Basic (Declaration)

```vb
Function RecordLine( _
   ByVal Text As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Text As System.String
Dim value As System.Boolean

value = instance.RecordLine(Text)
```

### C#

```csharp
System.bool RecordLine(
   System.string Text
)
```

### C++/CLI

```cpp
System.bool RecordLine(
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Text to write to a VBA macro and the SOLIDWORKS journal file

### Return Value

True if successful, false if not

## VBA Syntax

See [SldWorks::RecordLine](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RecordLine.html).

## Examples

[Record Macros (VBA)](Record_Macros_Example_VB.htm)
[Recor Macros (VB.NET)](Record_Macros_Example_VBNET.htm)
[Record Macros (C#)](Record_Macros_Example_CSharp.htm)

## Remarks

This method is useful if you want your add-in application to record and play back SOLIDWORKS macros or write to the SOLIDWORKS journal file.

For example, if your add-in application allows end users to change the material specifications associated with a model, then end users may want to be able to record and play back the operation in a macro. This might allow them to easily assign material specifications to a large number of files by playing back the macro.

Text is only written to macros if macro recording is enabled when the method is called ([ISldWorks::Run Command](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RunCommand.html) swCommands_RecordPauseMacro ""). Users are prompted to select the type of macros to create when recording is stopped (ISldWorks::Run Command swCommands_StopMacro "").

For your add-in functionality to be recorded reliably in all macro formats, you should call all three macro-recording methods:

- ISldWorks::RecordLine to record to a **SW VBA Macro (*.swp)**.
- [ISldWorks::RecordLineVBnet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RecordLineVBnet.html) to record to a **SW VSTA VB Macro (*.vbproj)**.
- [ISldWorks::RecordLineCSharp](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RecordLineCSharp.html) to record to a **SW VSTA C# Macro (*.csproj)**.

Exercise caution when recording lines that include string literals. String literals are parsed when the add-in application is compiled and again when the macro is compiled.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[DSldWorksEvents BeginRecordNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BeginRecordNotifyEventHandler.html)
[DSldWorks Events EndRecordNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_EndRecordNotifyEventHandler.html)
[ISldWorks::RunMacro2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro2.html)
