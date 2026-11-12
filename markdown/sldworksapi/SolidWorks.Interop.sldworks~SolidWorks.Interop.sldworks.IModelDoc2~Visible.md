---
title: "Visible Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Visible.html"
---

# Visible Property (IModelDoc2)

Gets or sets the visibility of the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get; set;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the document is visible, false if not

## VBA Syntax

See [ModelDoc2::Visible](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Visible.html).

## Examples

[Get Names of Open Documents (VBA)](Get_Names_of_Open_Documents_Example_VB.htm)
[Run or Attach to SOLIDWORKS Session (VBA)](SOLIDWORKS_Visible_or_BackGround_Example_VB.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)

## Remarks

User-interface resources are not released by setting this property to false. Opening large numbers of models and then hiding them using this property will eventually cause critical resource shortages and instability.

Instead of setting this property to false to hide a document, consider calling [ISldWorks::CloseDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html) to release its user-interface resources. Or open the document invisibly using [ISldWorks::DocumentVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DocumentVisible.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
