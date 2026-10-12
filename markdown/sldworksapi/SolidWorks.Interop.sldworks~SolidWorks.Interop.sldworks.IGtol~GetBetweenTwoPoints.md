---
title: "GetBetweenTwoPoints Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetBetweenTwoPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPoints.html"
---

# GetBetweenTwoPoints Method (IGtol)

Gets whether the between two points symbol is being used.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBetweenTwoPoints() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Boolean

value = instance.GetBetweenTwoPoints()
```

### C#

```csharp
System.bool GetBetweenTwoPoints()
```

### C++/CLI

```cpp
System.bool GetBetweenTwoPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if using the between two points symbol, false if not

## VBA Syntax

See [Gtol::GetBetweenTwoPoints](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetBetweenTwoPoints.html).

## Remarks

Use

- [IGtol::GetBetweenTwoPointsText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetBetweenTwoPointsText.html) to get the text that is used with this symbol.
- [IGtol::SetBetweenTwoPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetBetweenTwoPoints.html) to enable this symbol and its texts.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetBetweenTwoPointsText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPointsText.html)
[IGtol::SetBetweenTwoPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBetweenTwoPoints.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
