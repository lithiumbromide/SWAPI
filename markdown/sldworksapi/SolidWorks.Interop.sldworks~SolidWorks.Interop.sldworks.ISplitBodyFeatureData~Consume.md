---
title: "Consume Property (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "Consume"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~Consume.html"
---

# Consume Property (ISplitBodyFeatureData)

Gets or sets whether the bodies in this Split feature are consumed.

## Syntax

### Visual Basic (Declaration)

```vb
Property Consume As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim value As System.Boolean

instance.Consume = value

value = instance.Consume
```

### C#

```csharp
System.bool Consume {get; set;}
```

### C++/CLI

```cpp
property System.bool Consume {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the Split bodies are consumed, false if not

## VBA Syntax

See [SplitBodyFeatureData::Consume](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~Consume.html).

## Examples

[Create Split Feature (VBA)](Create_Split-body_Feature_Example_VB.htm)
[Create Split Feature (VB.NET)](Create_Split-body_Feature_Example_VBNET.htm)
[Create Split Feature (C#)](Create_Split-body_Feature_Example_CSharp.htm)

## Remarks

Consumed means the split bodies are removed from the part and do not appear in the Solid Bodies folder of the FeatureManager design tree.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[IFeatureManager::PostSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.html)
[IFeatureManager::PreSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
