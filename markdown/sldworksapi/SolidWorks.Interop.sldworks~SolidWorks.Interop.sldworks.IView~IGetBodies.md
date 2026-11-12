---
title: "IGetBodies Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBodies.html"
---

# IGetBodies Method (IView)

Gets the bodies of a multibody part in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBodies( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Count As System.Integer
Dim value As Body2

value = instance.IGetBodies(Count)
```

### C#

```csharp
Body2 IGetBodies(
   System.int Count
)
```

### C++/CLI

```cpp
Body2^ IGetBodies(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bodies of a multibody part in the drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IView::GetBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBodiesCount.html) to get the value of Count.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetBodies.html)
[IView::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Bodies.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
