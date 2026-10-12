---
title: "FrameNumber Property (IPMIFrameData)"
project: "SOLIDWORKS API Help"
interface: "IPMIFrameData"
member: "FrameNumber"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~FrameNumber.html"
---

# FrameNumber Property (IPMIFrameData)

Gets the index of this Gtol frame.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameNumber As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIFrameData
Dim value As System.Integer

instance.FrameNumber = value

value = instance.FrameNumber
```

### C#

```csharp
System.int FrameNumber {get; set;}
```

### C++/CLI

```cpp
property System.int FrameNumber {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Zero-based index of this Gtol frame

## VBA Syntax

See [PMIFrameData::FrameNumber](ms-its:sldworksapivb6.chm::/sldworks~PMIFrameData~FrameNumber.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.html)
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
