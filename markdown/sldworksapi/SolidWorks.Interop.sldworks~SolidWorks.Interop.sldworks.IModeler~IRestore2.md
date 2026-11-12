---
title: "IRestore2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IRestore2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore2.html"
---

# IRestore2 Method (IModeler)

Restores a temporary body object from the specified stream.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRestore2( _
   ByVal StreamIn As System.Object _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim StreamIn As System.Object
Dim value As Body2

value = instance.IRestore2(StreamIn)
```

### C#

```csharp
Body2 IRestore2(
   System.object StreamIn
)
```

### C++/CLI

```cpp
Body2^ IRestore2(
   System.Object^ StreamIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StreamIn`: IStream interface for storage inside the SOLIDWORKS document

### Return Value

Temporary [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::IRestore2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IRestore2.html).

## Remarks

You can use a temporary body object for display purposes. You can generate temporary bodies using such methods as [IModeler::CreateBodyFromFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBodyFromFaces2.html) or [IModeler::ICreateBodyFromFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html). Temporary bodies are not saved with the document unless you explicitly save them using [IBody2::Save](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Save.html) or [IBody2::ISave](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ISave.html).

You can obtain the StreamIn object by calling [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html) and by specifying the stream name that was used during the body save operation.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::Restore Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~Restore.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
