---
title: "UnloadAddIn Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "UnloadAddIn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnloadAddIn.html"
---

# UnloadAddIn Method (ISldWorks)

Unloads the specified add-in from SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Function UnloadAddIn( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Integer

value = instance.UnloadAddIn(FileName)
```

### C#

```csharp
System.int UnloadAddIn(
   System.string FileName
)
```

### C++/CLI

```cpp
System.int UnloadAddIn(
   System.String^ FileName
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `FileName`: Fully qualified file name of the add-in

### Return Value

Status of unloading the add-in:

- 0: Successfully unloaded the add-in
- -1: Failed to unload the add-in due to some error condition

## VBA Syntax

See

[SldWorks::UnloadAddIn](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~UnloadAddIn.html)

.

## Examples

[Load and Unload Add-in (C#)](Load_and_Unload_Add-in_Example_CSharp.htm)

[Load and Unload Add-in (VB.NET)](Load_and_Unload_Add-in_Example_VBNET.htm)

[Load and Unload Add-in (VBA)](Load_and_Unload_Add-in_Example_VB.htm)

## Remarks

You cannot unload MBD using its add-in path. Instead, unload the MBD add-in as follows:

status = swApp.**UnloadAddIn**('MBD')

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

[ISldWorks::LoadAddIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html)
