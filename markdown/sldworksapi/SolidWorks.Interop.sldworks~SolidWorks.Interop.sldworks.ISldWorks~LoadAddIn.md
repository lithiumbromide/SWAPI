---
title: "LoadAddIn Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "LoadAddIn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html"
---

# LoadAddIn Method (ISldWorks)

Loads the specified add-in in SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadAddIn( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Integer

value = instance.LoadAddIn(FileName)
```

### C#

```csharp
System.int LoadAddIn(
   System.string FileName
)
```

### C++/CLI

```cpp
System.int LoadAddIn(
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

Status of loading the add-in as defined in[swLoadAddinError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLoadAddinError_e.html)

## VBA Syntax

See

[SldWorks::LoadAddIn](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~LoadAddIn.html)

.

## Examples

[Load and Unload Add-in (C#)](Load_and_Unload_Add-in_Example_CSharp.htm)

[Load and Unload Add-in (VB.NET)](Load_and_Unload_Add-in_Example_VBNET.htm)

[Load and Unload Add-in (VBA)](Load_and_Unload_Add-in_Example_VB.htm)

## Remarks

You cannot load MBD using its add-in path. Instead, load the MBD add-in as follows:

status = swApp.**LoadAddIn**('MBD')

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

[ISldWorks::UnloadAddIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnloadAddIn.html)
