public class QuickSort {

// 平均时间复杂度 O(NlogN)
/**

* 快速排序调用方法

*

* @param ary 待排序数组

* @param left 左值

* @param right 右值

* @return int值

* @author Cansluck

*/

    public static int getSortNum(int[] ary, int left, int right) {

        // 定义一个中枢值pivot，让其等于数组的左值，枢轴选定后永远不变，最终在中间，前小后大

        int pivot = ary[left];
        int pIndex = left;

        while (left < right) {

        // 看后面ary[right] > pivot比较，如果右边数组值大于中枢值，说明不需要调整位置，则让右值（right）自减1

            while (left < right && ary[right] >= pivot) {

                right--; // 执行自减操作

            }

            // 如果上面循环不符合条件的，则说明右边数组的一个值，小于中枢值（pivot），则将其替换到左边数组中
            swap(ary, left, right);

            // 看后面ary[left] < pivot比较，如果左边数组值小于中枢值，说明不需要调整位置，则让左值（left）自增1

            while (left < right && ary[left] <= pivot) {

                left++; // 执行自增操作

            }

            // 如果上面循环不符合条件，则说明左边数组的一个值，大于中枢值（pivot），则将其替换到右边数组中

            swap(ary, right, left);

        }
        // 最后将中枢值给自增后的左边数组的一个值中
        ary[left] = pivot;
        // 返回左边数组下标
        return left;

    }
    
    private static void swap(int[] nums, int x, int y) {
        int temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
    }

    /**

    * 快速排序递归方法

    *

    * @author Cansluck

    * @param ary 待排序数组

    * @param left 左值

    * @param right 右值

    */

    public static void quickSort(int[] ary, int left, int right) {

        // 定义中枢值

        int pivot;

        // 判断

        if (left < right) {

            // 根据方法得到了每次中枢值的位置

            pivot = getSortNum(ary, left, right);

            // 根据中枢值（pivot），来对左边数组进行递归调用快速排序

            quickSort(ary, left, pivot - 1);

            // 根据中枢值（pivot），来对右边数组进行递归调用快速排序

            quickSort(ary, pivot + 1, right);

        }

    }

    public static void main(String[] args) {
        int[] ary = {97, 58, 12, 88, 77, 22, 33, 44, 66, 22};

        quickSort(ary, 0, ary.length - 1);

        int res = ary[ary.length - 2];
        System.out.println(ary);
        System.out.println(res);
    }

}