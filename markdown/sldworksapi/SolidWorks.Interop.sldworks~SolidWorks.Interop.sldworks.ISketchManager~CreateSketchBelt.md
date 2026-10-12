---
title: "CreateSketchBelt Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateSketchBelt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchBelt.html"
---

# CreateSketchBelt Method (ISketchManager)

Creates a sketch belt feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSketchBelt( _
   ByVal Length As System.Double, _
   ByVal Thickness As System.Double, _
   ByVal Engage As System.Integer, _
   ByVal PulleyCount As System.Integer, _
   ByVal Side1 As System.Integer, _
   ByVal Side2 As System.Integer, _
   ByVal Side3 As System.Integer, _
   ByVal Side4 As System.Integer, _
   ByVal Side5 As System.Integer, _
   ByVal Side6 As System.Integer, _
   ByVal Side7 As System.Integer, _
   ByVal Side8 As System.Integer, _
   ByVal Side9 As System.Integer, _
   ByVal Side10 As System.Integer, _
   ByVal Side11 As System.Integer, _
   ByVal Side12 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Length As System.Double
Dim Thickness As System.Double
Dim Engage As System.Integer
Dim PulleyCount As System.Integer
Dim Side1 As System.Integer
Dim Side2 As System.Integer
Dim Side3 As System.Integer
Dim Side4 As System.Integer
Dim Side5 As System.Integer
Dim Side6 As System.Integer
Dim Side7 As System.Integer
Dim Side8 As System.Integer
Dim Side9 As System.Integer
Dim Side10 As System.Integer
Dim Side11 As System.Integer
Dim Side12 As System.Integer
Dim value As System.Boolean

value = instance.CreateSketchBelt(Length, Thickness, Engage, PulleyCount, Side1, Side2, Side3, Side4, Side5, Side6, Side7, Side8, Side9, Side10, Side11, Side12)
```

### C#

```csharp
System.bool CreateSketchBelt(
   System.double Length,
   System.double Thickness,
   System.int Engage,
   System.int PulleyCount,
   System.int Side1,
   System.int Side2,
   System.int Side3,
   System.int Side4,
   System.int Side5,
   System.int Side6,
   System.int Side7,
   System.int Side8,
   System.int Side9,
   System.int Side10,
   System.int Side11,
   System.int Side12
)
```

### C++/CLI

```cpp
System.bool CreateSketchBelt(
   System.double Length,
   System.double Thickness,
   System.int Engage,
   System.int PulleyCount,
   System.int Side1,
   System.int Side2,
   System.int Side3,
   System.int Side4,
   System.int Side5,
   System.int Side6,
   System.int Side7,
   System.int Side8,
   System.int Side9,
   System.int Side10,
   System.int Side11,
   System.int Side12
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Length`: Length of the belt
- `Thickness`: Thickness of the belt
- `Engage`: 1 to engage the belt, 0 to not
- `PulleyCount`: Number of pulley components
- `Side1`: Place the belt for the corresponding pulley component :

  - 0 = inside
  - 1 = outside
- `Side2`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side3`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side4`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side5`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side6`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side7`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side8`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side9`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side10`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side11`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside
- `Side12`: Place the belt for the corresponding pulley component:

  - 0 = inside
  - 1 = outside

### Return Value

True the belt is created, false if not

## VBA Syntax

See [SketchManager::CreateSketchBelt](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~CreateSketchBelt.html).

## Remarks

The order of the sides corresponds to the order of the pulleys in the selection list. For example Side1 indicates on which side of the first pulley component in the selection list you want the belt placed. If only four pulley components exist in the sketch, then Side5 - Side12 are ignored. This method limits you to 12 pulleys.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
