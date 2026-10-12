---
title: "Restore Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "Restore"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~Restore.html"
---

# Restore Method (IModeler)

Restores a temporary body object from the specified stream.

## Syntax

### Visual Basic (Declaration)

```vb
Function Restore( _
   ByVal StreamIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim StreamIn As System.Object
Dim value As System.Object

value = instance.Restore(StreamIn)
```

### C#

```csharp
System.object Restore(
   System.object StreamIn
)
```

### C++/CLI

```cpp
System.Object^ Restore(
   System.Object^ StreamIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StreamIn`: IStream interface for storage inside the SOLIDWORKS document

## VBA Syntax

See [Modeler::Restore](ms-its:sldworksapivb6.chm::/sldworks~Modeler~Restore.html).

## Remarks

You can use a temporary body object for display purposes. You can generate temporary bodies using such methods as [IModeler::CreateBodyFromFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBodyFromFaces2.html) or [IModeler::ICreateBodyFromFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html). Temporary bodies are not saved with the document unless you explicitly save them using [IBody2::Save](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Save.html) or [IBody2::ISave](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ISave.html).

You can obtain the StreamIn object by calling [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html) and by specifying the stream name that was used during the body save operation.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::IRestore2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore2.html)
