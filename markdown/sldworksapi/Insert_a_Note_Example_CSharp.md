---
title: "Insert a Note Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_a_Note_Example_CSharp.htm"
---

# Insert a Note Example (C#)

This example shows show to insert a geometric tolerance symbol in an active drawing document.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 //
 // Postconditions:
 // 1. Inserts a geometric tolerance symbol is inserted at the specified position.
 // 2. Examine the graphics area.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //----------------------------------------------------------------------------
```

using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
namespace SetPosition2_CSharp.csproj
{

```vb
partial class  SolidWorksMacro
 {
```

```vb
public void Main()
 {
```

```vb
 ModelDoc2 Part =  default(ModelDoc2);
  Annotation Annotation =  default(Annotation);
 object swSelobj2 = null;
  SelectionMgr swSelMgr =  default(SelectionMgr);
 Note Note = default(Note);
 bool boolstatus = false;
 int longstatus = 0;

 Part = (ModelDoc2)swApp.ActiveDoc;
 swSelMgr = (SelectionMgr)Part.SelectionManager;
 boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.166288048468037, 0.223859686746988, -0.000400000000013279, false, 0, null, 0);
 swSelobj2 = swSelMgr.GetSelectedObject6(1, -1);
 Note = (Note)Part.InsertNote("<MOD-CL>");
 if ((Note != null))
 {
```

```vb
Note.Angle = 0;
 boolstatus = Note.SetBalloon(0, 0);
 Annotation = (Annotation)Note.GetAnnotation();
  object[] AttEntArr =  new object[1];
 AttEntArr[0] = swSelobj2;
  object vAttEntArrIn =  null;
 vAttEntArrIn = AttEntArr;
 boolstatus = Annotation.SetAttachedEntities(vAttEntArrIn);
 if ((Annotation != null))
 {
```

```vb
longstatus = Annotation.SetLeader3(1, 0, true, true, false, false);
 boolstatus = Annotation.SetPosition2(0.1038962799325, 0.135343450253, 0);
```

```vb
}
```

```vb
}
 Part.ClearSelection2(true);
 Part.WindowRedraw();
```

```vb
}

 public SldWorks swApp;
```

```vb
}
```

```vb
}
```
