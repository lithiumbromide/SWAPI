---
title: "FileName Property (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "FileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~FileName.html"
---

# FileName Property (ISwOLEObject)

Gets the path and name of the external file to which this OLE object is linked.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim value As System.String

value = instance.FileName
```

### C#

```csharp
System.string FileName {get;}
```

### C++/CLI

```cpp
property System.String^ FileName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and name of external file to which this OLE object is linked

## VBA Syntax

See [SwOLEObject::FileName](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~FileName.html).

## Examples

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html) examples.

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)
[ISwOLEObject::IsLinked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IsLinked.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
