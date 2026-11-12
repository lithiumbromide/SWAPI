---
title: "GetMouseDragMode Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetMouseDragMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMouseDragMode.html"
---

# GetMouseDragMode Method (ISldWorks)

Gets whether the specified command-mouse mode is in effect.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMouseDragMode( _
   ByVal Command As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Command As System.Integer
Dim value As System.Boolean

value = instance.GetMouseDragMode(Command)
```

### C#

```csharp
System.bool GetMouseDragMode(
   System.int Command
)
```

### C++/CLI

```cpp
System.bool GetMouseDragMode(
   System.int Command
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Command`: Command mode you wish to check as defined in [swMouseDragMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseDragMode_e.html)

### Return Value

True if the specified command is the currently running command, false if not

## VBA Syntax

See [SldWorks::GetMouseDragMode](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetMouseDragMode.html).

## Remarks

This method determines if a special mouse mode is in use. Generally, these mouse modes are indicated visually with a different cursor and different mouse input interpretation. For example, one such mode is View Rotate mode. This is indicated visually to the user with a different cursor. When in this mode, the mouse input manipulates interactive view rotation, and the View Rotate toolbar button is pressed.

A complete list of valid mouse modes can be found in the [swMouseDragMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseDragMode_e.html) enumeration.

The mouse mode applies to your whole SOLIDWORKS Design session, not a specific document. Therefore, if the user is currently working in an assembly document and is in Translate Assembly Component mode, then switching to a part or drawing document does not exit the mouse mode. If you call this method at this time to check for swTranslateAssemblyComponent, it returns True.

That mode is retained until a new command is entered, regardless if that this mode is not appropriate for a part or drawing document. When a new interactive command or API command runs, it terminates the Translate Assembly Component mode.

There is currently no general method to enable these mouse modes. However, several specific functions exist that enable or toggle certain modes. For example, [IAssemblyDoc::TranslateComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~TranslateComponent.html) and [IAssemblyDoc::RotateComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~RotateComponent.html). To disable any of these modes, use [IModelDoc2::SetPickMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetPickMode.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::SetMouseDragMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMouseDragMode.html)

## Availability

SOLIDWORKS 99, datecode 1999207
