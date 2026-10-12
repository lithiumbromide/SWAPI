---
title: "Attach Annotation to Entity Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Attach_Annotation_to_Entity_Example_CSharp.htm"
---

# Attach Annotation to Entity Example (C#)

This example shows how to attach a note to a different entity.

```
//-------------------------------------------------------
// Preconditions:
// 1. Open a part or drawing that has at least one
//    annotation that is a note.
// 2. Select the note.
// 3. Press Ctrl while selecting a face, edge, or vertex.
//
// Postconditions:
// 1. Attaches the selected note to the entity
//    selected in Preconditions step 3, if possible.
// 2. Examine the note in the graphics area.
//
// NOTE: If you open a drawing:
// * uncomment the statement for a drawing.
// * comment out the statement for a part.
//-------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetAttachedEntities.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            object swSelObj1 = null;
            object swSelObj2 = null;
            Annotation swAnn = default(Annotation);
            int[] vAttEntTypeArr = null;
            object[] vAttEntArr = null;
            int i = 0;
            bool bRet = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            //Select the note to move
            swSelObj1 = (object)swSelMgr.GetSelectedObject6(1, -1);
            Note swNote = default(Note);
            swNote = (Note)swSelObj1;
            swAnn = (Annotation)swNote.GetAnnotation();

            //Part - select the entity where to move the note
            swSelObj2 = (object)swSelMgr.GetSelectedObject6(2, -1);

            //Drawing - select the entity where to to move the note
            //swSelObj2 = (object)swSelMgr.GetSelectedObject6(3, -1);

            object[] AttEntArr = new object[1];
            AttEntArr[0] = swSelObj2;
            DispatchWrapper[] vAttEntArrIn = null;
            vAttEntArrIn = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray(AttEntArr);
            bRet = swAnn.SetAttachedEntities(vAttEntArrIn);
            Debug.Print("Name = " + swAnn.GetName());
            Debug.Print("  Selection Type = " + swSelMgr.GetSelectedObjectType3(1, -1));
            Debug.Print("  Annotation Type = " + swAnn.GetType());
            vAttEntArr = (object[])swAnn.GetAttachedEntities3();
            vAttEntTypeArr = (int[])swAnn.GetAttachedEntityTypes();
            if ((vAttEntTypeArr != null))
            {
                for (i = 0; i < vAttEntTypeArr.Length; i++)
                {
                    //A dangling dimension has at least one entity of type swSelNOTHING
                    Debug.Print("  Entity Type(" + i + ") = " + vAttEntTypeArr[i]);
                    SelectData swSelData = default(SelectData);
                    swSelData = (SelectData)swSelMgr.CreateSelectData();
                    Entity swEntity = default(Entity);
                    swEntity = (Entity)vAttEntArr[i];
                    swEntity.Select4(false, swSelData);
                }
            }

        }

        public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)
        {
            int ArraySize = 0;
            ArraySize = Objects.GetUpperBound(0);
            DispatchWrapper[] d = new DispatchWrapper[ArraySize + 1];
            int ArrayIndex = 0;
            for (ArrayIndex = 0; ArrayIndex <= ArraySize; ArrayIndex++)
            {
                d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);
            }
            return d;

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
