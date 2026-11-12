---
title: "Copy Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "Copy"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~Copy.html"
---

# Copy Property (IMoveCopyBodyFeatureData)

Gets or sets whether to copy the selected bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property Copy As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Boolean

instance.Copy = value

value = instance.Copy
```

### C#

```csharp
System.bool Copy {get; set;}
```

### C++/CLI

```cpp
property System.bool Copy {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to copy the selected bodies, false to not

## VBA Syntax

See [MoveCopyBodyFeatureData::Copy](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~Copy.html).

## Remarks

To get or set the number of copies of the selected bodies to create, call [IMoveCopyBodyFeatureData::NumberOfCopies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~NumberOfCopies.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
