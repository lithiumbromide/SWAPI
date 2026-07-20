---
title: "InsertGtol Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertGtol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertGtol.html"
---

# InsertGtol Method (IModelDoc2)

Creates a new geometric tolerance symbol (GTol) in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGtol() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.InsertGtol()
```

### C#

```csharp
System.object InsertGtol()
```

### C++/CLI

```cpp
System.Object^ InsertGtol();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Newly created

[GTol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html)

## VBA Syntax

See

[ModelDoc2::InsertGtol](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertGtol.html)

.

## Examples

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)

[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)

[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

## Remarks

The leader attachment point for the newly created GTol object comes from the selection made before calling this method. The initial location of the symbol is near the selection location. If there is no selection, then the GTol does not have a leader, is free standing, and is initially at the origin of the model or drawing.

This method creates an empty symbol. To fill in the text and symbols of this GTol, use the pointerkadov_tag{{</spaces>}}returned by this method to access the various get and set methods of the[IGTol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html)interface, such as[IGtol::SetFrameSymbols2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetFrameSymbols2.html)and[IGtol::SetFrameValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetFrameValues.html). Use[IGtol::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetAnnotation.html)to retrieve the[IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)object.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

[IModelDoc2::IInsertGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertGtol.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
