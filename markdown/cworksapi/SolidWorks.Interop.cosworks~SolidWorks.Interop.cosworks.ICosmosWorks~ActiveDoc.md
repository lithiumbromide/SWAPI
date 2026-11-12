---
title: "ActiveDoc Property (ICosmosWorks)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICosmosWorks"
member: "ActiveDoc"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICosmosWorks~ActiveDoc.html"
---

# ActiveDoc Property (ICosmosWorks)

Gets the model document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ActiveDoc As CWModelDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosWorks
Dim value As CWModelDoc

value = instance.ActiveDoc
```

### C#

```csharp
CWModelDoc ActiveDoc {get;}
```

### C++/CLI

```cpp
property CWModelDoc^ ActiveDoc {
   CWModelDoc^ get();
}
```

### Property Value

[Model document](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWModelDoc.html)

## VBA Syntax

See [CosmosWorks::ActiveDoc](ms-its:cworksapivb6.chm::/CosmosWorksLib~CosmosWorks~ActiveDoc.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICosmosWorks Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICosmosWorks.html)
[ICosmosWorks Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICosmosWorks_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
