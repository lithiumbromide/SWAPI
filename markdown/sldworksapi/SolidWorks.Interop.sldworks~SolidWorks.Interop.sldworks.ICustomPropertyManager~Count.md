---
title: "Count Property (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Count"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Count.html"
---

# Count Property (ICustomPropertyManager)

Gets the number of custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Count As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim value As System.Integer

value = instance.Count
```

### C#

```csharp
System.int Count {get;}
```

### C++/CLI

```cpp
property System.int Count {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 or the number of custom properties

## VBA Syntax

See [CustomPropertyManager::Count](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Count.html).

## Examples

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)
[Get Custom Properties for Cut-list Item (VBA)](Get_Custom_Properties_for_Cut-list_Item_Example_VB.htm)

## Remarks

Call this method before calling [ICustomPropertyManager::IGetNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~IGetNames.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
